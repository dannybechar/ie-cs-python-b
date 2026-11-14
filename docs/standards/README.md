# Standards

[Table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

Governing rules for the whole repository. They are summarised here and kept where they were written; nothing was moved.

| Standard | Where it lives |
|---|---|
| Content authority: the official Python B program in the classroom-downloader folder and the Ministry's published teaching materials decide topics, order, terminology and exercises; the program PDF decides official hours (master table) | [`CLAUDE.md`](../../CLAUDE.md), [`docs/ministry-teaching-materials.md`](../ministry-teaching-materials.md), [`docs/ministry-source/`](../ministry-source) |
| Year-wide pedagogy: phases, depth boundaries, tools, exit profile | [`docs/annual-strategy.md`](../annual-strategy.md) |
| Naming rule: meetings are named by the range of **official lesson numbers** (Lessons 8.0–8.1 — Strings; Hebrew שיעורים 8.0–8.1 – מחרוזות), the theme only as a subtitle; never "מפגש" or "פרק" | [`docs/official-numbering.md`](../official-numbering.md) |
| Code conventions: every `.py` compiles; `_Starter` / `_Reference`; only what the class has been taught; no API keys | [`CLAUDE.md`](../../CLAUDE.md) ("Conventions") |
| Hebrew in Markdown: start each line with a Hebrew word, code in fenced blocks, tables and lists in `<div dir="rtl">` | [`CLAUDE.md`](../../CLAUDE.md) ("Conventions") |
| Time budget: every lesson states Duration and Structure; unit minutes equal official minutes (1 academic hour = 45 min) | [`course-map.md`](../../course-map.md) |
| Unit layout and teacher-only rule | [`units/README.md`](../../units/README.md) |

## Lesson deck standard (HTML)

Every lesson page `lessons/L<NN>-<slug>.md` has a generated `L<NN>-<slug>.html` beside it (same stem).

- One self-contained file: inline CSS and JavaScript, no external fonts, scripts or images; works offline from a double-click.
- One idea per slide (split at each `##` heading); Previous and Next buttons; keyboard navigation (in these right-to-left decks the left arrow, space and Page Down go forward, the right arrow and Page Up go back).
- Readable in light and dark (`prefers-color-scheme`) and on a phone (no horizontal scrolling); printing gives one slide per page.
- Student-safe: built only from the student lesson page, never from `teacher/`; any section headed Solution, Answer key or Teacher (also in Hebrew) is dropped.
- Start with `<!doctype html>`, `<meta charset="utf-8">` and a viewport meta; the `<title>` is the lesson's title.
- No new PDF or PowerPoint is produced for the generated lesson page. The existing PDFs (NotebookLM decks, live-lesson decks, printed worksheets) are course deliverables kept in `lessons/L<NN>-<slug>/`; the patch workflow is in [`tools/deck-patch-kit/`](../../tools/deck-patch-kit/README.md).

GitHub shows `.html` files as source, not as a rendered page: open a downloaded copy in a browser.
