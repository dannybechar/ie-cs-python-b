# Countdown page (teacher tool)

The countdown method from the teacher's IB DP1 and PDP classes, for this course: timed in-class cases projected one at a time.
A case is opened (goal, the starter file, its test values, how to get the files), a big clock runs (green, amber, red),
the room is locked out at zero ("ננעל!"), and the reveal shows a `for` solution and a `while` solution that use different
ideas, the expected output, and how the two differ. Hebrew, right-to-left; code in Courier New, left-to-right.

Cases are **plain code, no functions** (Lessons 8.2–8.7 were taught before the class learned `def`): a variable `text = "…"`,
the student's code under it, and `print`. To test another value, students change the variable and run again, as DP1's
"statements inside `main`" problems do.

Everything a student or the projector sees is **generated** — never edit it by hand:

- `<unit>/<mN>-countdown-cases.json`: title, subtitle, footer, unit, the steps to get the files, and per case: the starter
  file name, an English goal (the starter's comment), Hebrew title and goal, minutes, tools used, test values, how the two
  solutions differ; plus the names of the reference file, the page and the instructions.
- the reference `.py`: sections `# === case N for ===` and `# === case N while ===`, each starting with `text = "…"`.
  The build replaces that line with every test value, runs both versions, stops if they print different things,
  and uses what they print as the expected output.
- `countdown_template.html` (here): the page itself.

```
python tools/countdown/build_countdown.py units/u5-strings/m4-countdown-cases.json
```

It writes the page, the students' instructions (Markdown — goal, file, test values, expected output, no solutions) and one
starter file per case. Turn the instructions into a PDF with `python tools/md_to_docx.py <md> <docx> --worksheet` and
`soffice --headless --convert-to pdf`, and zip the PDF with the starters for Mashov. Python 3, standard library only.
Rebuild and commit after any change to the JSON, the reference or the template.

Used by: [Lessons 8.2–8.7 countdown edition](../../units/u5-strings/m4-countdown-lesson-plan.md).
