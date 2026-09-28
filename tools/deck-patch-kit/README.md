# Deck patch kit

Tools for reviewing and patching the Hebrew slide decks that NotebookLM generates for this course.
Teacher-facing material lives in `units/`; this folder is only for maintaining the decks.
The kit was built for the Grade 7 Python A course (`ie-cs-python-a`, 31 decks) and carried over unchanged
except for the Grade 9 settings in `mkinstr.py`.

Requirements: Python 3 with `pymupdf`, `pillow`, `numpy`, `opencv-python`, `python-bidi`; Windows fonts Segoe UI and Consolas.

| File | What it is |
|---|---|
| `common.py` | `render`, `load`/`save`/`build`, `sheet`, `erase`, `inpaint`, `inpaint_rect`, `detect`, `text_color`/`dark`, `font_h`/`fit_w`, `draw_v`, `parts` |
| `heb.py` | `visual()`: a logical Hebrew line in on-screen (left-to-right) order; Pillow here has no raqm, so text is drawn exactly as given |
| `mkinstr.py` | writes a NotebookLM folder's `0-START-HERE-instructions.md` |
| `examples/p94.py`, `examples/p96.py` | two real patch scripts (Python A decks 9.4 and 9.6): timer badges, garbled mixed Hebrew/code lines, axis labels, removing decorative code |
| `examples/find_rows.py` | prints the pixel boxes of the text rows in a region (to aim erases and redraws) |

## Review and patch one deck

1. Copy `common.py` and `heb.py` to the session scratchpad and work there.
2. Render the newest PDF in Downloads: `render(pdf, D)` (D is a short tag such as `21` for Unit 2.1).
3. **Check the title slide first** — the newest PDF may be a different meeting than the one asked for,
   and NotebookLM names files by theme (e.g. `Python_Scope_Mission.pdf`), not by unit.
4. Check every slide against `Downloads/python-b-unit<U>-m<M>-slides/1-source-slide-content.md`
   (or, when that folder is gone, the lesson notes and the `_Reference` code): use `sheet()` for overviews, then crop suspicious lines at full size.
5. Write `p<D>.py` (`from common import *`) that patches only real errors, `save(D, p, im)` each page, then `build(D, '', N)`.
   Look at every patched page at full size before building; a wide inpaint mask can eat neighbouring text.
6. Copy `new_<D>.pdf` to `units/<unit dir>/m<M>-slides-he.pdf` and to `Downloads/python-b/unit U.M - <English unit name>.pdf`;
   update the unit README row and the `course-map.md` meeting log; commit and push.

## Drawing Hebrew

- `parts(im, runs, baseline, right=... | center=... | left=...)` draws runs in **on-screen left-to-right order**.
  Hebrew runs go through `V()` (words reversed, each word's letters reversed); code runs stay literal.
  Example: the line "הפעולה `move_up()` מזיזה" is `[(V('מזיזה') + ' ', H, W), ('move_up()', M, W), (' ' + V('הפעולה'), H, W)]`.
- Hebrew in Segoe UI (`FR`, bold `FB`), code in Consolas (`MONO`). Match size with `font_h(FR, px, probe=V('word'))`
  and colour with `text_color()` (light text) or `dark()` (dark text).
- Shrink to fit with a loop over sizes until `sum(f.getlength(t) for t, f, c in runs) <= width`.
- Plain bidi (`GD`) flips expressions such as `17 // 5` into `5 // 17`; build mixed lines by hand with `parts()`.

## Recurring NotebookLM problems

- Hebrew lines that mix in code come out garbled (flipped parentheses, doubled or made-up words). Rebuild them with `parts()` in on-screen order.
- The footer sits under the Gemini watermark (bottom right). Redraw it to the left or centered.
- Table columns in left-to-right order. Swap the column strips when the widths match.
- Pictures that contradict the code (3D houses, nested squares, a wrong windmill, a zigzag `goto`, a closed shape for an open path). Redraw the flat Turtle result.
- A challenge-task slide that shows the full (sometimes wrong) solution. Keep only the function header.
- Minus signs dropped from answers (`-5`, `-6`), and "X" written on the vertical axis. Check every number and axis label.
- Decorative code from outside the course (pygame, JavaScript) in the background. Remove it.
- Timer badges with a stray colon or without the number.
- Hints or picture text that give away the answer on a question-only slide. Remove them.
- A "bug" slide where NotebookLM silently fixed the bug. Restore the bug.
- Missing timers on student-activity slides. Copy the deck's own timer badge.
- Arrows drawn backwards (new value → old value). Mirror the arrow strip.
- Dropped slides: NotebookLM caps decks near 21 slides. Keep sources at ≤ 20 slides, and build a missing tail slide from the deck's own last slide as a template.

## Preparing a NotebookLM folder

`mkinstr.make(...)` writes `0-START-HERE-instructions.md` (Hebrew output language, the exact NAMING block, slide count,
code and table rules, check list). Set `GRADE`, `CODE_STYLE` and the `theme` argument for this course before using it.
Each `Downloads/python-b-unit<U>-m<M>-slides/` folder also gets `1-source-slide-content.md`
(every slide spelled out, minutes summing to 90) and the meeting's lesson notes and Hebrew lab brief.
