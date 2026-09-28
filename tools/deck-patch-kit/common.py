# NotebookLM deck patch kit (Grade 8 AI + Python B course; first used for Grade 7 Python A). See README.md in this folder.
# Needs: pymupdf, pillow, numpy, opencv-python, python-bidi.
# Work in a scratch folder: copy common.py and heb.py there, render the deck into <D>/pNN.png,
# write p<D>.py with `from common import *`, then build(D, '', N) -> new_<D>.pdf.
import numpy as np, fitz, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from heb import visual
import cv2
FB, FR = "C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/segoeui.ttf"
MONO = 'C:/Windows/Fonts/consola.ttf'
V = visual


def GD(s):
    """bidi visual order for a mixed Hebrew/Latin line (RTL base)."""
    from bidi.algorithm import get_display
    return get_display(s, base_dir='R')


def render(pdf, deck):
    """render every page to <deck>/pNN.png at 1376x768; returns the page count"""
    d = fitz.open(pdf); os.makedirs(deck, exist_ok=True)
    for i, p in enumerate(d):
        p.get_pixmap(matrix=fitz.Matrix(1376/p.rect.width, 768/p.rect.height)).save(f'{deck}/p{i+1:02d}.png')
    return len(d)


def load(deck, p): return np.asarray(Image.open(f'{deck}/p{p:02d}.png').convert('RGB')).astype(float)
def to_img(a): return Image.fromarray(a.clip(0, 255).astype(np.uint8))
def save(deck, p, im): os.makedirs(f'out{deck}', exist_ok=True); im.save(f'out{deck}/p{p:02d}.png')


def build(deck, relpath, n):
    """PDF from out<deck>/ (patched) or <deck>/ (untouched) pages -> new_<deck>.pdf"""
    doc = fitz.open()
    for p in range(1, n+1):
        src = f'out{deck}/p{p:02d}.png' if os.path.exists(f'out{deck}/p{p:02d}.png') else f'{deck}/p{p:02d}.png'
        pg = doc.new_page(width=1376, height=768); pg.insert_image(pg.rect, filename=src)
    out = f'new_{deck}.pdf'; doc.save(out, deflate=True, garbage=4); return out


def sheet(deck, pages, name, out=True):
    """contact sheet (two per row, half size) for visual checks"""
    ims = [Image.open(f'{"out" if out else ""}{deck}/p{p:02d}.png').resize((688, 384)) for p in pages]
    S = Image.new('RGB', (1376, 384*((len(ims)+1)//2)))
    for i, im in enumerate(ims): S.paste(im, ((i % 2)*688, (i//2)*384))
    S.save(name)


def smooth_rows(c, k=9):
    p = k//2; cp = np.pad(c, ((p, p), (0, 0)), mode='edge'); ker = np.ones(k)/k
    return np.stack([np.convolve(cp[:, ch], ker, mode='valid') for ch in range(c.shape[1])], 1)


def erase(a, x0, x1, y0, y1, k=9):
    """horizontal interpolation between the columns just outside [x0,x1)"""
    L = smooth_rows(a[y0:y1, x0-5:x0].mean(1), k); R = smooth_rows(a[y0:y1, x1:x1+5].mean(1), k)
    t = np.linspace(0, 1, x1-x0)[None, :, None]; a[y0:y1, x0:x1] = L[:, None]*(1-t)+R[:, None]*t


def erase_v(a, x0, x1, y0, y1, k=9):
    """vertical interpolation between the rows just outside [y0,y1)"""
    T = smooth_rows(a[y0-5:y0, x0:x1].mean(0), k); B = smooth_rows(a[y1:y1+5, x0:x1].mean(0), k)
    t = np.linspace(0, 1, y1-y0)[:, None, None]; a[y0:y1, x0:x1] = T[None]*(1-t)+B[None]*t


def inpaint(a, x0, x1, y0, y1, thr=110, dil=6, radius=7, mask_fn=None):
    """inpaint the text pixels in the box (mask = max channel > thr, or mask_fn(region)), dilated"""
    reg = a[y0:y1, x0:x1]
    m = (mask_fn(reg) if mask_fn else reg.max(2) > thr).astype(np.uint8)*255
    m = cv2.dilate(m, np.ones((2*dil+1, 2*dil+1), np.uint8))
    full = np.zeros(a.shape[:2], np.uint8); full[y0:y1, x0:x1] = m
    img = cv2.cvtColor(a.clip(0, 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    out = cv2.inpaint(img, full, radius, cv2.INPAINT_TELEA)
    a[:] = cv2.cvtColor(out, cv2.COLOR_BGR2RGB).astype(float)


def inpaint_rect(a, x0, x1, y0, y1, exclude=None, radius=6):
    full = np.zeros(a.shape[:2], np.uint8); full[y0:y1, x0:x1] = 255
    if exclude: ex0, ex1, ey0, ey1 = exclude; full[ey0:ey1, ex0:ex1] = 0
    img = cv2.cvtColor(a.clip(0, 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    a[:] = cv2.cvtColor(cv2.inpaint(img, full, radius, cv2.INPAINT_TELEA), cv2.COLOR_BGR2RGB).astype(float)


BR = lambda t: (lambda g: g.max(2) > t)   # bright text mask (dark slides)
DK = lambda t: (lambda g: g.max(2) < t)   # dark text mask (light slides)


def detect(a, x0, x1, y0, y1, thr=170, mask=None):
    """bbox of text pixels (mean > thr, or mask fn) inside the window: ((x0,x1,y0,y1), mask) or None"""
    reg = a[y0:y1, x0:x1]
    m = mask(reg) if mask else reg.mean(2) > thr
    ys = np.where(m.sum(1) >= 2)[0]; xs = np.where(m.sum(0) >= 1)[0]
    if len(ys) == 0: return None
    return (x0+xs.min(), x0+xs.max()+1, y0+ys.min(), y0+ys.max()+1), m


def text_color(a, bb):
    """color of bright text in the box"""
    x0, x1, y0, y1 = bb; reg = a[y0:y1, x0:x1].reshape(-1, 3); br = reg.mean(1)
    sel = reg[br >= np.percentile(br, 93)]; return tuple(int(v) for v in sel.mean(0))


def dark(a, bb):
    """color of dark text in the box"""
    x0, x1, y0, y1 = bb; r = a[y0:y1, x0:x1].reshape(-1, 3); b = r.mean(1)
    return tuple(int(v) for v in r[b <= np.percentile(b, 4)].mean(0))


def font_h(path, height, probe='הדיחי0'):
    """font whose probe text is ~height px tall"""
    s = 8
    while True:
        b = ImageFont.truetype(path, s+1).getbbox(probe)
        if b[3]-b[1] > height: return ImageFont.truetype(path, s)
        s += 1


def fit_w(path, vis, width):
    """largest font whose visual string fits the width"""
    sz = 10
    while ImageFont.truetype(path, sz+1).getlength(vis) <= width: sz += 1
    return ImageFont.truetype(path, sz)


def draw_v(im, vis, font, fill, top, right=None, center=None, left=None, glow=None, r=5, strength=0.6):
    """draw an already-visual-order string; top = top of its glyph box"""
    w = font.getlength(vis); bb = font.getbbox(vis)
    x = (right-w) if right is not None else (left if left is not None else center-w/2)
    xy = (x, top-bb[1])
    if glow:
        g = Image.new('RGB', im.size, (0, 0, 0)); ImageDraw.Draw(g).text(xy, vis, font=font, fill=glow)
        g = g.filter(ImageFilter.GaussianBlur(r)); im = to_img(np.asarray(im).astype(float)+np.asarray(g).astype(float)*strength)
    ImageDraw.Draw(im).text(xy, vis, font=font, fill=fill); return im


def text(im, line, font, fill, top, **kw):
    """draw a logical Hebrew line (reordered with visual())"""
    return draw_v(im, visual(line), font, fill, top, **kw)


def parts(im, items, base, right=None, left=None, center=None):
    """draw runs [(visual_text, font, color), ...] in on-screen left-to-right order on one baseline.
    For a Hebrew line with code, list the runs as they appear on screen, e.g.
    'show_title() מדפיסה === GAME ===.' ->
    [('.', H, W), ('=== GAME ===', M, W), (' ' + V('מדפיסה') + ' ', H, W), ('show_title()', H, C)]"""
    w = sum(f.getlength(t) for t, f, c in items)
    x = right-w if right is not None else (left if left is not None else center-w/2); d = ImageDraw.Draw(im)
    for t, f, c in items: d.text((x, base), t, font=f, fill=c, anchor='ls'); x += f.getlength(t)
    return im
