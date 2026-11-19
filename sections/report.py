"""Report page: the written report, chapter by chapter, with its figures."""
import re
import streamlit as st
from config import REPORT_DIR, ROOT

CHAPTERS = [("Abstract", "abstract"), ("Introduction", "introduction"), ("Literature Review", "literature_review"),
            ("Methodology", "methodology"), ("Results", "results"), ("Discussion", "discussion"),
            ("Conclusion", "conclusion"), ("Appendix", "appendix"), ("References", "references")]
IMG = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
BLOCK = re.compile(r"\$\$\s*(.+?)\s*\$\$", re.S)


def _text(chunk):
    """Markdown text; display equations ($$...$$) are drawn with st.latex."""
    if "[Equation: see the Word report]" in chunk:
        st.warning("This report content is out of date (equations were not converted). "
                   "Re-run: python tools/rebuild_report.py \"your_report.docx\"")
    pos = 0
    for m in BLOCK.finditer(chunk):
        if chunk[pos:m.start()].strip():
            st.markdown(chunk[pos:m.start()])
        for line in m.group(1).split("\n"):
            if line.strip():
                st.latex(line.strip())
        pos = m.end()
    if chunk[pos:].strip():
        st.markdown(chunk[pos:])


def _render(text):
    pos = 0
    for m in IMG.finditer(text):
        _text(text[pos:m.start()])
        path = ROOT / m.group(1)
        if path.exists():
            st.image(str(path), use_container_width=True)
        pos = m.end()
    _text(text[pos:])


def render():
    st.header("Machine Learning Approach for Identification of At-Risk Students")
    st.caption("Diploma in Civil Engineering, Cape Peninsula University of Technology")
    available = [(t, k) for t, k in CHAPTERS if (REPORT_DIR / f"{k}.md").exists() and (REPORT_DIR / f"{k}.md").read_text(encoding="utf-8").strip()]
    if not available:
        st.warning("No report content found. Run: python tools/rebuild_report.py \"your_report.docx\"")
    else:
        for tab, (_, key) in zip(st.tabs([t for t, _ in available]), available):
            with tab:
                _render((REPORT_DIR / f"{key}.md").read_text(encoding="utf-8"))
    with st.expander("Update report from a new Word document"):
        up = st.file_uploader("Upload the updated .docx", type=["docx"], key="report_docx")
        if up is not None and st.button("Rebuild report from this file"):
            from tools.rebuild_report import rebuild
            info, n = rebuild(up)
            st.success(f"Rebuilt {len(info)} chapters and {n} figures.")
            st.rerun()
