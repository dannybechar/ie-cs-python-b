# Writes <folder>/0-START-HERE-instructions.md for one NotebookLM deck. See README.md.
GRADE = "8th graders (age 13–14)"
# Code-style rule pasted into the prompt. Grade 8 AI + Python B: no Turtle objects, and API keys never appear in code.
CODE_STYLE = "Write every Python line exactly as in the source — names, f-strings, operators and spacing. Never invent an API key, a real person's name or real personal data."


# Official lesson labels (docs/official-numbering.md): file key (U, M) -> official lessons. U and M still select the meeting.
LESSONS = {
    (1, 1): "1.0–1.1",
    (1, 2): "1.2–1.4",
    (1, 3): "2.0–2.3",
    (2, 1): "3.0–3.1",
    (2, 2): "3.1–3.2",
    (3, 1): "4.1–4.2",
    (3, 2): "4.4–4.5",
    (3, 3): "4.3, 4.6",
    (4, 1): "5.0–5.2",
    (4, 2): "6.1–6.2",
    (5, 1): "7.1",
    (5, 2): "7.1–7.2",
    (5, 3): "8.0–8.1",
    (5, 4): "8.2–8.7",
    (6, 1): "10.0–10.2",
    (6, 2): "11.1–11.2",
    (6, 3): "11.3",
    (7, 1): "9.1, 9.4",
    (7, 2): "9.3, 9.5, 12.0–12.1",
    (7, 3): "12.6, 13.0–13.1",
    (7, 4): "13.2, 14.0–14.2",
    (7, 5): "12.5, 14.4",
    (8, 1): "16.0–16.2",
    (8, 2): "17.0–17.1",
    (8, 3): "18.0–18.1",
    (8, 4): "19.0–19.1",
    (9, 1): "20.0–20.1",
    (9, 2): "21.1",
    (9, 3): "21.1–21.2",
    (9, 4): "22.0–22.1",
}


def make(folder, U, M, name_en, name_he, subtitle, n, topic, theme, qonly, checks, saves, notebook_he, extra_forbid, unitdir, raw, raw_issue):
    les = LESSONS[(U, M)]
    word_he = "שיעורים" if ("–" in les or "," in les) else "שיעור"
    word_en = "Lessons" if ("–" in les or "," in les) else "Lesson"
    title = f"{word_he} {les} – {name_he}"
    s = f'''# {word_en} {les} — {name_en} slides — NotebookLM instructions

> ## ⚠️ THE PRESENTATION MUST BE IN HEBREW
> **המצגת חייבת להיות בעברית.** Every title, sentence, question and instruction on the slides is in Hebrew.
> Only code, commands, file names, `True` / `False` and program output stay in English.
> **Step 2 below is not optional.**

---

## 1. Create the notebook

New notebook: **{word_en} {les} — {name_en} · {notebook_he}**

## 2. Set the output language to Hebrew

In NotebookLM's settings, set the **output language** to **עברית (Hebrew)**. Check this **before** generating.

## 3. Add these 3 sources (all in this folder)

| # | File | What it is |
|---|---|---|
| 1 | `1-source-slide-content.md` | All {n} slides: titles, text, code, outputs, tables, minutes. **The main source** |
| 2 | `m{M}-lesson-notes.md` | Teacher lesson plan (background) |
| 3 | `m{M}-lab-brief-he.md` | Hebrew student lab brief (wording to match) |

If NotebookLM won't accept a `.md` upload, open the file, copy everything, and add it as **Copied text**.

> [!WARNING]
> **Do not add the raw decks** (`{raw}`) as sources. {raw_issue}

## 4. Generate the slide deck

Choose **Slide Deck** and paste this into **"Describe the slide deck that you want to create"**:

```text
LANGUAGE: The entire presentation must be in HEBREW (עברית). Every title, sentence, question, label and instruction on every slide is in Hebrew. Only code, commands, file names, True / False and program output stay in English, exactly as written in the sources, left-to-right.

NAMING (exact): The title slide's main title is "{title}" and its subtitle is "{subtitle}". Every slide, including the title slide, has the footer "{title}". Do not use "מפגש", "פרק", "יחידה" or any other meeting label.

SLIDES: Build exactly {n} slides — one slide per "### Slide" section in the source "{word_en} {les} slide content", in the same order. Never merge two sections, never skip one: the last slides (exit check and exit answers) must be included. This is a Python lesson for {GRADE}: {topic}. Copy every title, text, code block, output block and table exactly — do not reword, shorten or translate them.

CODE: Keep every code block's line breaks and 4-space indentation exactly as in the source. Use only straight double quotes (") in code — never curly quotes (“ ” or ‘ ’). Never show code fences (```) as text. {CODE_STYLE}

TABLES: Keep every table's columns in the source order and put each value in its own column. In empty tables for students, leave the answer cells empty.

Theme: {theme}. Use the theme for titles and pictures only; never change code, outputs or instructions.

Style: bold, clean, big code, one idea per slide, max 4 short lines of text. Student-activity slides show a timer with exactly the minutes given, written as "N דקות"; no timers on other slides. On "question only" slides, do NOT show the answer, output or filled-in table; the answer is on the next slide. Do not add {extra_forbid} or any content that is not in the sources.
```

## 5. Check the new deck before class

- [ ] **All slide text is in Hebrew.**
- [ ] **Exactly {n} slides**, ending with the exit check and its answers.
- [ ] Slide 1 title "{title}", subtitle "{subtitle}".
- [ ] Footer "{title}" on every slide.
- [ ] Straight quotes `"` in every code block (no “ ”); indentation visible.
- [ ] Question-only slides ({qonly}) show no answers or filled tables.
- [ ] Timers only on student-activity slides.
'''
    for c in checks: s += f'- [ ] {c}\n'
    s += f'''- [ ] Save name: `{saves}`.
- [ ] No {extra_forbid} or visible ``` marks; code matches the source exactly.

## 6. When it's ready

Save the PDF in Downloads and tell Claude. It will check the deck against this list, patch anything left, add it to the repo as `units/{unitdir}/m{M}-slides-he.pdf`, and log it in `course-map.md`.
'''
    open(f'{folder}/0-START-HERE-instructions.md', 'w', encoding='utf-8', newline='').write(s)
