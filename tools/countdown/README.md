# Countdown page (teacher tool)

The countdown method from the teacher's IB DP1 and PDP classes, for this course: timed in-class cases projected one at a time.
A case is opened (goal, the function to write, its test calls, how to get the file), a big clock runs (green, amber, red),
the room is locked out at zero ("ננעל!"), and the reveal shows a `for` solution and a `while` solution that use different
ideas, the expected output, and how the two differ. Hebrew, right-to-left; code in Courier New, left-to-right.

The page is one standalone HTML file per lesson (no login, no internet). It is **generated** — never edit it by hand:

- `<unit>/<mN>-countdown-cases.json`: title, subtitle, footer, the steps to get the file, and per case: function name, Hebrew
  title and goal, minutes, tools used, test calls, how the two solutions differ; plus the names of the reference and
  starter files and of the output page.
- the reference `.py`: `<func>_for` and `<func>_while` for every case (comment lines are dropped on the reveal screen).
- the starter `.py`: a `<func>` stub for every case (shown on the briefing screen).
- `countdown_template.html` (here): the page itself.

```
python tools/countdown/build_countdown.py units/u5-strings/m4-countdown-cases.json
```

The build runs every test call on both versions, stops if they disagree, and writes the results as the expected output.
Python 3, standard library only. Rebuild and commit after any change to the JSON, the reference or the template.

Used by: [Unit 5.4 countdown edition](../../units/u5-strings/m4-countdown-lesson-plan.md).
