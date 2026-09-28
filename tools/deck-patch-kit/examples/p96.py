# Example from the Grade 7 course (ie-cs-python-a): the patch script for deck 9.6. Pixel boxes are specific to that deck.
from common import *
D = '96'
W = (245, 250, 250)
ORANGE = lambda g: (g[..., 0] > 170) & (g[..., 0] - g[..., 2] > 60)

# p2: "4 : דקות" -> "4 דקות" (drop the colon, close the gap)
a = load(D, 2)
inpaint(a, 236, 253, 37, 110, mask_fn=ORANGE, dil=3, radius=4)
reg = a[35:112, 262:312].copy(); m = ORANGE(reg)
inpaint(a, 262, 312, 35, 112, mask_fn=ORANGE, dil=3, radius=4)
t = a[35:112, 232:282]; t[m] = reg[m]
save(D, 2, to_img(a))

# p13: ": 3 דקות" -> "3 דקות"
a = load(D, 13)
inpaint_rect(a, 1232, 1260, 588, 652)
save(D, 13, to_img(a))


def fit(make, width, hi=40, lo=12):
    for z in range(hi, lo, -1):
        r = make(z)
        if sum(f.getlength(t) for t, f, c in r) <= width: return r
    return make(lo)


def fonts(h):
    H = font_h(FR, h, probe=V('מחוברות'))
    return H, ImageFont.truetype(MONO, H.size - 2)


# p8: checkpoint A items garbled (numbers at the right are kept)
a = load(D, 8)
inpaint(a, 115, 615, 265, 660, thr=150, dil=3, radius=4)
im = to_img(a)
R = 606
def lines(z):
    H = ImageFont.truetype(FR, z); M = ImageFont.truetype(MONO, z - 2)
    return [
        (298, [('move_down()', M, W), ('-' + V('ו') + ' ', H, W), ('move_up()', M, W)]),
        (334, [(V('מחוברות לחצים, וכל תזוזה'), H, W)]),
        (370, [('.', H, W), ('check_hit()', M, W), (' ' + V('מזמנת את'), H, W)]),
        (426, [(V('לחיצה על המסך') + ' — ', H, W), ('place_target(x, y)', M, W)]),
        (463, [(V('מעבירה את המטרה.'), H, W)]),
        (518, [(V('ספירה לאחור של 30') + ' — ', H, W), ('tick()', M, W)]),
        (555, [(V('והניקוד.') + ' ', H, W), ('Game over', H, W), (' ' + V('שניות, ובסוף'), H, W)]),
        (606, [(V('הצב לא זז:') + ' ', H, W), ('Game over', H, W), (' ' + V('אחרי'), H, W)]),
        (646, [(V('בכל תזוזה.') + ' ', H, W), ('if running:', M, W)]),
    ]
for z in range(30, 12, -1):
    L = lines(z)
    if max(sum(f.getlength(t) for t, f, c in r) for b, r in L) <= 480: break
print('p8 size', z)
for b, r in L: im = parts(im, r, b, right=R)
save(D, 8, im)

# p10: questions 2 and 4 garbled
a = load(D, 10)
C = text_color(a, (964, 1260, 280, 298))
inpaint(a, 740, 1277, 276, 302, thr=120, dil=3, radius=4)
inpaint(a, 740, 1277, 444, 473, thr=120, dil=3, radius=4)
im = to_img(a)
F = lambda z: ImageFont.truetype(FR, z)
im = parts(im, fit(lambda z: [('?' + V('מה יודפס') + ' .', F(z), C), ('tick()', F(z), C), (' ' + V('ואז') + ' ,', F(z), C),
                              ('time_left = 3', F(z), C)], 1262 - 745, hi=21), 297, right=1262)
im = parts(im, fit(lambda z: [('?' + V('אין') + ' ', F(z), C), ('move_up()', F(z), C),
                              ('-' + V('ול') + ' ' + V('יש פרמטרים') + ' ', F(z), C),
                              ('place_target(x, y)', F(z), C), ('-' + V('ל') + ' ' + V('למה'), F(z), C)], 1262 - 745, hi=21),
           467, right=1262)
save(D, 10, im)

# p11: gibberish labels, answer 1 in the wrong order, answers 3-4 outside their boxes
a = load(D, 11)
C = text_color(a, (1098, 1270, 198, 217))
MC = text_color(a, (850, 1280, 319, 339))
inpaint(a, 740, 1277, 194, 222, thr=120, dil=3, radius=4)
inpaint(a, 780, 1292, 232, 259, thr=150, dil=3, radius=4)
inpaint(a, 740, 1277, 278, 301, thr=120, dil=3, radius=4)
inpaint(a, 740, 1300, 400, 476, thr=150, dil=4, radius=5)
inpaint(a, 740, 1300, 562, 604, thr=150, dil=4, radius=5)
im = to_img(a)
F = lambda z: ImageFont.truetype(FR, z)
MF = lambda z: ImageFont.truetype(MONO, z)
im = parts(im, fit(lambda z: [(V('איזה מאזין לכל אירוע?'), F(z), C)], 400, hi=21), 216, right=1264)
im = parts(im, fit(lambda z: [('turtle.ontimer · turtle.onscreenclick · turtle.onkey', MF(z), MC)], 500, hi=20), 253, right=1286)
im = parts(im, fit(lambda z: [(V('מה יודפס?'), F(z), C)], 400, hi=21), 297, right=1264)
im = parts(im, fit(lambda z: [('?', F(z), C), ('turtle.onkey(move_up(), "Up")', F(z), C),
                              ('-' + V('ב') + ' ' + V('מה לא בסדר'), F(z), C), (' .3', F(z), C)], 540, hi=21), 466, right=1296)
im = parts(im, fit(lambda z: [(V('הסוגריים מריצים את הפונקציה עכשיו — מוסרים רק את השם.'), F(z), W)], 500, hi=20), 502, right=1284)
im = parts(im, fit(lambda z: [('?' + V('אין') + ' ', F(z), C), ('move_up()', F(z), C), ('-' + V('ול') + ' ' + V('פרמטרים') + ' ', F(z), C),
                              ('place_target', F(z), C), ('-' + V('ל') + ' ' + V('למה יש'), F(z), C), (' .4', F(z), C)], 540, hi=21),
           596, right=1296)
im = parts(im, fit(lambda z: [('.' + V('מקש לא שולח כלום') + ' ;y-' + V('ו') + ' x ' + V('לחיצה שולחת'), F(z), W)], 500, hi=20),
           630, right=1284)
save(D, 11, im)

# p15: pygame code in the background (never taught) -> remove it, keep the subtitle and the targets
a = load(D, 15)
KEEP = lambda g: ((g[..., 0] > 150) & (g[..., 1] < 110)) | ((g[..., 1] > 170) & (g[..., 2] > 170) & (g[..., 0] < 110))
CODE = lambda g: (g.max(2) > 62) & ~KEEP(g)
for x0, x1, y0, y1 in [(138, 560, 55, 235), (830, 1310, 45, 165), (880, 975, 195, 225), (890, 1305, 255, 285),
                       (218, 350, 496, 522), (218, 690, 524, 640), (1022, 1170, 488, 512), (860, 1090, 518, 542),
                       (860, 960, 546, 570)]:
    inpaint(a, x0, x1, y0, y1, mask_fn=CODE, dil=3, radius=4)
save(D, 15, to_img(a))

build(D, '', 15)
sheet(D, [2, 8, 10, 11], 'i1.png'); sheet(D, [13, 15], 'i2.png')
