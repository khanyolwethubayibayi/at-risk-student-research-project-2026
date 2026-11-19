"""Convert Word equations (OMML) to LaTeX so Streamlit can display them."""
import re

M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
SYMBOLS = {"α": r"\alpha ", "β": r"\beta ", "γ": r"\gamma ", "δ": r"\delta ", "ε": r"\varepsilon ", "θ": r"\theta ",
           "λ": r"\lambda ", "μ": r"\mu ", "π": r"\pi ", "σ": r"\sigma ", "χ": r"\chi ", "Σ": r"\sum ", "∑": r"\sum ",
           "∏": r"\prod ", "…": r"\dots ", "⋯": r"\cdots ", "×": r"\times ", "·": r"\cdot ", "≤": r"\le ",
           "≥": r"\ge ", "≈": r"\approx ", "≠": r"\ne ", "∈": r"\in ", "→": r"\to ", "∞": r"\infty ",
           "√": r"\sqrt ", "−": "-", "–": "-", "\u00a0": " "}
PHRASE = re.compile(r"[A-Za-z][A-Za-z' \-]*[A-Za-z]")


def _text(s):
    s = s.replace("\u200b", "")
    out, pos = [], 0
    for m in PHRASE.finditer(s):
        out.append(_symbols(s[pos:m.start()]))
        out.append(r"\text{" + m.group(0).strip() + "}")
        pos = m.end()
    out.append(_symbols(s[pos:]))
    return "".join(out)


def _symbols(s):
    return "".join(SYMBOLS.get(c, c) for c in s).replace("%", r"\%").replace("&", r"\&").replace("#", r"\#")


def _kids(e, name):
    return [c for c in e if c.tag == M + name]


def _body(e):
    """LaTeX of every math child of an element (skipping its properties)."""
    return "".join(_node(c) for c in e if not c.tag.endswith("Pr"))


def _chr(pr, name, default):
    if pr is not None:
        c = pr.find(M + name)
        if c is not None:
            return c.get(M + "val", "")
    return default


def _node(e):
    t = e.tag.split("}")[1]
    if t == "r":
        return _text("".join(x.text or "" for x in e.findall(M + "t")))
    if t == "sSub":
        return "{" + _body(_kids(e, "e")[0]) + "}_{" + _body(_kids(e, "sub")[0]) + "}"
    if t == "sSup":
        return "{" + _body(_kids(e, "e")[0]) + "}^{" + _body(_kids(e, "sup")[0]) + "}"
    if t == "sSubSup":
        return ("{" + _body(_kids(e, "e")[0]) + "}_{" + _body(_kids(e, "sub")[0]) + "}^{"
                + _body(_kids(e, "sup")[0]) + "}")
    if t == "f":
        return r"\frac{" + _body(_kids(e, "num")[0]) + "}{" + _body(_kids(e, "den")[0]) + "}"
    if t == "eqArr":
        rows = [_body(r) for r in _kids(e, "e")]
        return r"\begin{aligned}" + r" \\ ".join(rows) + r"\end{aligned}"
    if t == "nary":
        pr = e.find(M + "naryPr")
        op = _symbols(_chr(pr, "chr", "∑")).strip() or r"\int"
        sub, sup = _kids(e, "sub"), _kids(e, "sup")
        lim = ("_{" + _body(sub[0]) + "}" if sub and _body(sub[0]) else "") + \
              ("^{" + _body(sup[0]) + "}" if sup and _body(sup[0]) else "")
        return op + lim + " {" + _body(_kids(e, "e")[0]) + "}"
    if t == "d":
        pr = e.find(M + "dPr")
        beg, end, sep = _chr(pr, "begChr", "("), _chr(pr, "endChr", ")"), _chr(pr, "sepChr", "|")
        parts = [_body(x) for x in _kids(e, "e")]
        if beg == "{" and end == "" and len(_kids(e, "e")) == 1 and _kids(e, "e")[0].find(M + "eqArr") is not None:
            rows = [_body(r) for r in _kids(_kids(e, "e")[0].find(M + "eqArr"), "e")]
            return r"\begin{cases}" + r" \\ ".join(rows) + r"\end{cases}"
        fix = lambda c, left: ("." if c == "" else (r"\{" if c == "{" else (r"\}" if c == "}" else c)))
        return r"\left" + fix(beg, True) + (" " + sep + " ").join(parts) + r"\right" + fix(end, False)
    if t in ("oMath", "e", "num", "den", "sub", "sup"):
        return _body(e)
    return ""


def omml_to_latex(e):
    return _body(e).strip()
