# Live-deck builder

Turns a `1-source-slide-content.md` (the same format as the NotebookLM prep folders) into a 16:9 Hebrew slide-deck PDF,
without NotebookLM: one slide per `### Slide N` section, code boxes in bold Courier New (left-to-right), outputs in a dark
terminal box, red timer badge on `Timer` slides, footer "יחידה 5.1 – מחרוזות", letter boxes with indices on slides 7–8.

```text
python -X utf8 tools/live-deck/build_deck.py <1-source-slide-content.md> deck.html
msedge --headless --no-pdf-header-footer --print-to-pdf=deck.pdf file:///<path>/deck.html
```

- Used for the Unit 5.1 live lesson ([`m1-live-slides-he.pdf`](../../units/u5-strings/m1-live-slides-he.pdf)).
- The footer text and the slide numbers that get the letter-box picture (`n in (7, 8)`) and the numbered list (`n == 19`)
  are hard-coded for Unit 5.1: edit them for another unit.
- A code block followed by its output is shown side by side when the lines are short; very tall outputs split in two columns.
- Look at every page after building (the font size is computed per slide, long lines can still come out small).
