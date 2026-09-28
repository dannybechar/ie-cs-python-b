import re
HEB = re.compile(r"[֐-׿]")
def visual(s):
    """Logical Hebrew line -> left-to-right visual order (no shaping needed for Hebrew)."""
    toks = s.split(" ")
    out = []
    for t in toks:
        out.append(t[::-1] if HEB.search(t) else t)
    return " ".join(reversed(out))
