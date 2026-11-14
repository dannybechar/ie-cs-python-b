# Lesson decks

[Table of contents](../../CONTENTS.md) · [Standards](../../docs/standards/README.md)

`build_decks.py` writes one self-contained HTML slide deck beside every lesson page: `units/*/lessons/L<NN>-<slug>.md` gives `L<NN>-<slug>.html`.
The Markdown page (the student's Hebrew lab brief) is the source of truth; the HTML is generated and must not be edited by hand.

```
pip install -r requirements.txt     # the Python "markdown" package
python tools/lesson-decks/build_decks.py            # rebuild all decks
python tools/lesson-decks/build_decks.py --check    # exit 1 if a deck is missing or out of date
```

Run it without `-I` (isolated mode hides user-installed packages). After a lesson page changes, rebuild and commit the `.html` with it.

- Slides: a title slide (heading and intro), then one slide per `##` section. Lines inside code fences never split a slide.
- Right to left (`lang="he" dir="rtl"`), code blocks and inline code stay left to right; GitHub-style `> [!NOTE]` boxes become coloured boxes.
- Student-safe: it reads only the student lesson page. Sections whose heading contains Solution, Answer key or Teacher (or the Hebrew פתרון, מפתח תשובות, למורה) are dropped; none of the current pages has such a section. A plain "answer" is not a trigger, so student tasks like "critique the answer" stay.
- Verified in headless Edge: layout in dark mode, slide counter, and that printing gives one page per slide (sample deck checked: Python A Unit 4.1). Not opened in a phone browser.
