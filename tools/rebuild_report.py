"""Convert the Word report into report_content/*.md and assets/figures/*.

Usage:  python tools/rebuild_report.py "path/to/report.docx"
The Heading 1 titles listed in CHAPTER_MAP start a new chapter file; the abstract is the text under
the 'ABSTRACT' subtitle. Rename a chapter in Word? Update CHAPTER_MAP to match.
"""
import re
import shutil
import sys
from pathlib import Path

import docx
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.omml import M, W, omml_to_latex
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_MAP = {"introduction": "introduction", "literature review": "literature_review",
               "methodology": "methodology", "results": "results", "results and discussion": "results",
               "discussion": "discussion", "conclusion and recommendations": "conclusion",
               "conclusion": "conclusion", "appendix": "appendix", "references": "references"}
HEADINGS = {"Heading 2": "##", "Heading 3": "###", "Heading 4": "####"}


def _table_md(tbl):
    rows = [[c.text.strip().replace("\n", " ").replace("|", "/") for c in r.cells] for r in tbl.rows]
    if not rows or not rows[0]:
        return ""
    w = len(rows[0])
    rows = [(r + [""] * w)[:w] for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * w]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def _chapter_key(text):
    t = re.sub(r"[^a-z ]", "", text.lower()).strip()
    return "appendix" if t.startswith("appendix") else CHAPTER_MAP.get(t)


def para_text(el):
    """Text of a paragraph in order, with equations as LaTeX ($inline$ and $$display$$)."""
    out = []

    def walk(node):
        for c in node:
            tag = c.tag
            if tag == W + "r":
                for x in c:
                    if x.tag == W + "t":
                        out.append(x.text or "")
                    elif x.tag in (W + "tab", W + "br"):
                        out.append(" ")
                    elif x.tag == W + "noBreakHyphen":
                        out.append("-")
            elif tag in (W + "hyperlink", W + "ins", W + "smartTag"):
                walk(c)
            elif tag == M + "oMath":
                out.append("$" + omml_to_latex(c) + "$")
            elif tag == M + "oMathPara":
                eqs = [omml_to_latex(x) for x in c if x.tag == M + "oMath"]
                out.append("\n\n$$\n" + "\n".join(eqs) + "\n$$\n\n")

    walk(el)
    return "".join(out)


def rebuild(src, root=ROOT):
    root = Path(root)
    d = docx.Document(src)
    fig_dir, out_dir = root / "assets" / "figures", root / "report_content"
    for p in (fig_dir, out_dir):
        shutil.rmtree(p, ignore_errors=True)
        p.mkdir(parents=True, exist_ok=True)
    chapters, state = {}, {"cur": None, "fig": 0}

    def add(line):
        if state["cur"]:
            chapters.setdefault(state["cur"], []).append(line)

    def walk(parent):
        for child in parent.iterchildren():
            tag = child.tag.split("}")[1]
            if tag == "sdt":
                content = child.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sdtContent")
                if content is not None:
                    walk(content)
            elif tag == "p":
                para(Paragraph(child, d), child)
            elif tag == "tbl" and state["cur"]:
                add(_table_md(Table(child, d)) + "\n")

    def para(p, el):
        style = p.style.name if p.style is not None else ""
        text = para_text(el).strip()
        if style == "Heading 1":
            key = _chapter_key(text)
            state["cur"] = key or state["cur"]
            if state["cur"]:
                chapters.setdefault(state["cur"], [])
            return
        if style == "Subtitle" and text.upper() == "ABSTRACT":
            state["cur"] = "abstract"
            chapters.setdefault("abstract", [])
            return
        if not state["cur"] or style.lower().startswith(("toc", "table of figures")) or text.startswith("[You may insert"):
            return
        for rid in el.xpath(".//a:blip/@r:embed"):
            part = d.part.related_parts.get(rid)
            ext = Path(str(part.partname)).suffix.lower() if part is not None else ""
            if ext in (".png", ".jpg", ".jpeg"):
                state["fig"] += 1
                name = f"fig{state['fig']:03d}{ext}"
                (fig_dir / name).write_bytes(part.blob)
                add(f"![figure](assets/figures/{name})\n")
        if not text:
            return
        if style in HEADINGS:
            add(f"{HEADINGS[style]} {text}\n")
        elif style == "Caption":
            add(f"*{text}*\n")
        elif style == "List Paragraph" and not text.startswith("$$"):
            add(f"- {text}")
        else:
            add(text + "\n")

    walk(d.element.body)
    for key, lines in chapters.items():
        (out_dir / f"{key}.md").write_text("\n".join(lines), encoding="utf-8")
    return {k: len(v) for k, v in chapters.items()}, state["fig"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    info, n = rebuild(sys.argv[1])
    print(f"Wrote {len(info)} chapters and {n} figures:", info)
