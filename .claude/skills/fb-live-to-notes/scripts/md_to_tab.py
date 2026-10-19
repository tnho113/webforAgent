#!/usr/bin/env python3
"""Chuyển một file Markdown đơn giản thành request `update_doc` để ghi vào một tab Google Docs trống.

Hỗ trợ: "# ", "## ", "### " (tiêu đề), "- " (gạch đầu dòng), "1. " (đánh số),
lồng danh sách bằng 2 dấu cách mỗi cấp, **đậm**, *nghiêng*, và một bảng dạng
"| a | b |" (dòng thứ hai "|---|" bị bỏ qua). Mỗi đoạn văn thường là một dòng.

Bảng không được chèn trong lượt này: script in ra vị trí và ghi rows.json để chèn
bằng `docs_index.py new-table` sau khi đọc lại doc.

Dùng: python3 md_to_tab.py notes.md --tab TAB_ID --revision REV --out req.json
"""
import argparse
import json
import re

INLINE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*")


def u16(s):
    return len(s.encode("utf-16-le")) // 2


def parse_inline(s):
    """Trả về (chữ đã bỏ dấu, [(start, end, bold, italic)] theo UTF-16)."""
    out, spans, pos = "", [], 0
    for m in INLINE.finditer(s):
        out += s[pos:m.start()]
        txt, bold = (m.group(1), True) if m.group(1) is not None else (m.group(2), False)
        spans.append((u16(out), u16(out) + u16(txt), bold, not bold))
        out += txt
        pos = m.end()
    return out + s[pos:], spans


def parse(md):
    paras, table, table_after = [], [], None
    for raw in md.splitlines():
        if not raw.strip():
            continue
        if raw.lstrip().startswith("|"):
            cells = [c.strip() for c in raw.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c) for c in cells):
                continue
            if not table:
                table_after = len(paras) - 1
            table.append([parse_inline(c)[0] for c in cells])
            continue
        indent = (len(raw) - len(raw.lstrip(" "))) // 2
        line = raw.strip()
        style, kind = "NORMAL_TEXT", None
        for prefix, st in (("### ", "HEADING_3"), ("## ", "HEADING_2"), ("# ", "HEADING_1")):
            if line.startswith(prefix):
                style, line = st, line[len(prefix):]
                break
        else:
            if line.startswith("- "):
                kind, line = "ul", line[2:]
            elif re.match(r"\d+\. ", line):
                kind, line = "ol", line.split(" ", 1)[1]
        text, spans = parse_inline(line)
        paras.append(dict(style=style, kind=kind, level=indent if kind else 0, text=text, spans=spans))
    return paras, table, table_after


def build(paras, tab, rev):
    text, pos, info = "", 1, []
    style_reqs, text_reqs = [], []
    for p in paras:
        prefix = "\t" * p["level"]
        start = pos
        chunk = prefix + p["text"] + "\n"
        end = pos + u16(chunk)
        text += chunk
        base = start + len(prefix)
        if p["style"] != "NORMAL_TEXT":
            style_reqs.append({"updateParagraphStyle": {
                "range": {"startIndex": start, "endIndex": end, "tabId": tab},
                "paragraphStyle": {"namedStyleType": p["style"]}, "fields": "namedStyleType"}})
        for s, e, bold, italic in p["spans"]:
            text_reqs.append({"updateTextStyle": {
                "range": {"startIndex": base + s, "endIndex": base + e, "tabId": tab},
                "textStyle": {"bold": bold, "italic": italic}, "fields": "bold,italic"}})
        info.append(dict(start=start, end=end, kind=p["kind"], level=p["level"]))
        pos = end
    text = text[:-1]  # đoạn cuối dùng ký tự xuống dòng có sẵn của tab
    blocks, cur = [], None
    for i in info:
        if i["kind"]:
            if cur is None:
                cur = dict(start=i["start"], end=i["end"], kind=i["kind"])
                blocks.append(cur)
            cur["end"] = i["end"]
        else:
            cur = None
    # Áp bullet từ dưới lên: dấu tab bị xóa khi tạo bullet làm dịch các vị trí phía sau.
    bullet_reqs = [{"createParagraphBullets": {
        "range": {"startIndex": b["start"], "endIndex": b["end"], "tabId": tab},
        "bulletPreset": "NUMBERED_DECIMAL_ALPHA_ROMAN" if b["kind"] == "ol" else "BULLET_DISC_CIRCLE_SQUARE"}}
        for b in reversed(blocks)]
    reqs = [{"insertText": {"location": {"index": 1, "tabId": tab}, "text": text}},
            {"updateParagraphStyle": {"range": {"startIndex": 1, "endIndex": pos, "tabId": tab},
                                      "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}},
            {"updateTextStyle": {"range": {"startIndex": 1, "endIndex": pos - 1, "tabId": tab},
                                 "textStyle": {}, "fields": "bold,italic"}}]
    return {"requests": reqs + style_reqs + text_reqs + bullet_reqs, "writeControl": {"requiredRevisionId": rev}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--tab", required=True)
    ap.add_argument("--revision", required=True)
    ap.add_argument("--out", default="req.json")
    ap.add_argument("--rows", default="rows.json")
    a = ap.parse_args()
    paras, table, after = parse(open(a.md, encoding="utf-8").read())
    json.dump(build(paras, a.tab, a.revision), open(a.out, "w"), ensure_ascii=False)
    print(f"{a.out}: {len(paras)} đoạn")
    if table:
        json.dump(table, open(a.rows, "w"), ensure_ascii=False)
        print(f"{a.rows}: bảng {len(table)}x{len(table[0])}, chèn sau đoạn: {paras[after]['text'][:60]!r}")


if __name__ == "__main__":
    main()
