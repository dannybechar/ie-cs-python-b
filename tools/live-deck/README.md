# Live-deck builder

Turns a `1-source-slide-content.md` (the same format as the NotebookLM prep folders) into a 16:9 Hebrew slide-deck PDF,
without NotebookLM: one slide per `### Slide N` section, code boxes in bold Courier New (left-to-right), outputs in a dark
terminal box, red timer badge on `Timer` slides, footer "שיעור 7.1 – מחרוזות", letter boxes with indices on slides 7–8.

```text
python -X utf8 tools/live-deck/build_deck.py <1-source-slide-content.md> deck.html --footer "שיעורים 7.1–7.2 – מחרוזות" ^
    --subtitle "<subtitle>" --emoji "<emoji>" [--card <word>] [--boxes 7,8 --boxes-word ROBOT] [--numbered 19]
msedge --headless --no-pdf-header-footer --print-to-pdf=deck.pdf file:///<path>/deck.html
```

Options: `--scale 1.3` (multiplies every font size) and `--stack` (code above output, full width): both used for the one-slide projected challenge; `--no-title` (slide 1 is a normal slide, not the title slide; used by the Lessons 8.2–8.7 deck), `--footer` (also the title), `--subtitle` and `--emoji` (title slide), `--card` (a word in a card on the title slide),
`--boxes` (slide numbers that show the letter boxes with indices, for the word given by `--boxes-word`), `--numbered`
(slides whose bullets are a numbered list, e.g. the exit check).

- Used for the live lessons of Lesson 7.1, Lessons 7.1–7.2 and Lessons 8.0–8.1 ([`m1-live-slides-he.pdf`](../../units/u5-strings/m1-live-slides-he.pdf), [`m2-`](../../units/u5-strings/m2-live-slides-he.pdf), [`m3-`](../../units/u5-strings/m3-live-slides-he.pdf)).
- A code block followed by its output is shown side by side when the lines are short; very tall outputs split in two columns.
- Look at every page after building (the font size is computed per slide, long lines can still come out small).
