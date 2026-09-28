# Prints the pixel boxes (y0, y1, x0, x1) of the text rows inside a region of a rendered page,
# to aim inpaint boxes and pick baselines. Run from the scratch folder next to common.py.
# Usage: rows('21', 7, 190, 1190, 220, 630)   # deck tag, page, x0, x1, y0, y1; thr=170 finds light text
from common import *


def rows(deck, p, x0, x1, y0, y1, thr=170, light=True):
    a = load(deck, p); g = a[y0:y1, x0:x1].mean(2)
    m = g > thr if light else g < thr
    r = m.sum(1) > 1; out = []; s = None
    for i, v in enumerate(list(r) + [False]):
        if v and s is None: s = i
        if not v and s is not None:
            if i - s > 4:
                xs = np.where(m[s:i].sum(0) > 0)[0]; out.append((y0+s, y0+i, x0+xs.min(), x0+xs.max()+1))
            s = None
    print(p, out)
    return out
