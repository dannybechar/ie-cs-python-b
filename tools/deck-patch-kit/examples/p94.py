# Example from the Grade 7 course (ie-cs-python-a): the patch script for deck 9.4. Pixel boxes are specific to that deck.
from common import *
D = '94'
ORANGE = lambda g: (g[..., 0] > 150) & (g[..., 0] - g[..., 2] > 60)


def orange_of(a, x0, x1, y0, y1):
    reg = a[y0:y1, x0:x1]; m = ORANGE(reg)
    return tuple(int(v) for v in np.median(reg[m], 0))


def fit_runs(make, width, lo=14, hi=80):
    """largest size whose runs fit the width; make(size) -> runs"""
    for s in range(hi, lo, -1):
        r = make(s)
        if sum(f.getlength(t) for t, f, c in r) <= width: return r
    return make(lo)


# p5: check 2 ends with two question marks
a = load(D, 5)
inpaint(a, 1036, 1060, 408, 458, thr=150, dil=3, radius=4)
save(D, 5, to_img(a))

# p7: the key list leaves out "Left"
a = load(D, 7)
OR = orange_of(a, 637, 1207, 140, 190); WH = (253, 253, 253)
inpaint(a, 600, 1318, 136, 194, thr=120, dil=4, radius=5)
im = to_img(a)
runs = fit_runs(lambda s: [('.', ImageFont.truetype(FB, s), WH),
                           ('"Up", "Down", "Left", "Right"', ImageFont.truetype(FB, s), OR),
                           (' :' + V('שמות המקשים'), ImageFont.truetype(FB, s), WH)], 1310 - 560, hi=44)
im = parts(im, runs, 180, right=1310)
save(D, 7, im)

# p10: title garbled "(left)" and "- 200"
a = load(D, 10)
OR = orange_of(a, 657, 1310, 85, 145)
inpaint(a, 640, 1318, 78, 148, thr=120, dil=4, radius=5)
im = to_img(a)
runs = fit_runs(lambda s: [('.-200 ' + V('עם גבול של') + ' ', ImageFont.truetype(FB, s), WH),
                           ('left()', ImageFont.truetype(FB, s), OR),
                           (' ' + V('כתבו את'), ImageFont.truetype(FB, s), WH)], 1310 - 640, hi=56)
im = parts(im, runs, 132, right=1310)
save(D, 10, im)


def axis_y(a, box, bright):
    """replace an axis label 'X' on the vertical axis with 'Y'"""
    x0, x1, y0, y1 = box
    col = text_color(a, box) if bright else dark(a, box)
    inpaint(a, x0 - 3, x1 + 3, y0 - 3, y1 + 3, mask_fn=(BR(120) if bright else DK(150)), dil=2, radius=3)
    im = to_img(a)
    F = font_h(FR, y1 - y0, probe='Y')
    ImageDraw.Draw(im).text(((x0 + x1) / 2, y1), 'Y', font=F, fill=col, anchor='ms')
    return im


# p15: subtitle garbled; vertical axis labelled X
a = load(D, 15)
inpaint(a, 540, 1325, 120, 198, thr=150, dil=4, radius=5)
im = axis_y(a, (690, 711, 234, 254), True)
C = (251, 254, 254)
H = font_h(FR, 26, probe=V('שמאלה וימינה'))
im = parts(im, [('up(), down(), left(), right()', H, C), (' — ' + V('ארבע פונקציות'), H, C)], 154, right=1318)
im = parts(im, [(V('שמאלה וימינה.') + ' ,200 ' + V('לבין') + ' -200 ' + V('הצב נשאר בין'), H, C)], 190, right=1318)
save(D, 15, im)

# p16: task text garbled ("(toggle_pen():", "pen_on = not" split)
a = load(D, 16)
inpaint(a, 800, 1315, 175, 465, thr=150, dil=4, radius=5)
im = to_img(a)
C = (250, 254, 254)
H = font_h(FR, 30, probe=V('פונקציה'))
M = ImageFont.truetype(MONO, H.size)
R = 1305
im = parts(im, [('toggle_pen()', M, C), (' ' + V('פונקציה בשם'), H, C)], 216, right=R)
im = parts(im, [(V('מקש רווח מחליף בין ציור'), H, C)], 266, right=R)
im = parts(im, [(V('לתנועה בלי ציור.'), H, C)], 314, right=R)
im = parts(im, [(V('הערך מתחלף כך:'), H, C)], 395, right=R)
im = parts(im, [('pen_on = not pen_on', M, C)], 445, right=R)
save(D, 16, im)

# p17: vertical axis labelled X (dark text on the white panel)
a = load(D, 17)
save(D, 17, axis_y(a, (690, 715, 295, 320), False))

build(D, '', 19)
sheet(D, [5, 7, 10, 15], 'g1.png'); sheet(D, [16, 17], 'g2.png')
