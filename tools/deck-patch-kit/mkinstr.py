# Writes <folder>/0-START-HERE-instructions.md for one NotebookLM deck. See README.md.
GRADE = "9th graders (age 14–15)"
# Code-style rule pasted into the prompt. Grade 9 uses turtle.Turtle() objects and Turtle subclasses (Unit 2 on),
# so the rule is "exactly as in the source" rather than Grade 7's "never t = turtle.Turtle()".
CODE_STYLE = "Write every Python line exactly as in the source — names, objects (turtle.Turtle(), class definitions), operators and spacing."


def make(folder, U, M, name_en, name_he, subtitle, n, topic, theme, qonly, checks, saves, notebook_he, extra_forbid, unitdir, raw, raw_issue):
    title = f"יחידה {U}.{M} – {name_he}"
    s = f'''# Unit {U}.{M} — {name_en} slides — NotebookLM instructions

> ## ⚠️ THE PRESENTATION MUST BE IN HEBREW
> **המצגת חייבת להיות בעברית.** Every title, sentence, question and instruction on the slides is in Hebrew.
> Only code, commands, file names, `True` / `False` and program output stay in English.
> **Step 2 below is not optional.**

---

## 1. Create the notebook

New notebook: **Unit {U}.{M} — {name_en} · {notebook_he}**

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

NAMING (exact): The title slide's main title is "{title}" and its subtitle is "{subtitle}". Every slide, including the title slide, has the footer "{title}". Do not use "מפגש", "שיעור", "פרק" or any other unit or meeting label.

SLIDES: Build exactly {n} slides — one slide per "### Slide" section in the source "Unit {U}.{M} slide content", in the same order. Never merge two sections, never skip one: the last slides (exit check and exit answers) must be included. This is a Python lesson for {GRADE}: {topic}. Copy every title, text, code block, output block and table exactly — do not reword, shorten or translate them.

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
