# Mock quiz — answers (release to students after they practise)

Practice sheet: [`strings-quiz-mock-he.md`](../assessment/strings-quiz-mock-he.md). Verified code: [`StringsQuizMock_Solution.py`](solutions/StringsQuizMock_Solution.py) (Python 3.14). Same 24 / 16 / 30 / 30 split as the real quiz.

| Q | Answer |
|---|---|
| 1a | `lep` · `ant` · `eehn` · `3` · `True` · `ElEphant` |
| 1b | prints `elephant`: `upper()` returns a new string; `word` is not changed (the result was thrown away) |
| 2a | `IndexError: string index out of range`; the last place is `len(name) - 1`, so use `name[len(name) - 1]` or `name[-1]` |
| 2b | prints `la la la`; `replace` returns a new string. Fix: `song = song.replace("la", "na")` |

```python
# Q3
code = "ab-2045-xy"
place = code.find("-")
print("Prefix:", code[:place])
print("Rest:", code[place + 1:])
print("Upper:", code.upper())
print("Dashes:", code.count("-"))
print("Has 2045:", "2045" in code)
```

```python
# Q4
sentence = "Strings are fun"

count = 0
for ch in sentence:
    if ch.lower() == "s":
        count += 1
print("S count:", count)

new = ""
for ch in sentence:
    if ch == "n":
        new += "*"
    else:
        new += ch
print("Stars:", new)

for i in range(len(sentence)):
    if sentence[i] == "r":
        print("Place:", i)
```

Common mistakes: `code[place:]` gives `-2045-xy` (forgot `+ 1`); `range(len(sentence) + 1)` crashes; `new = ch` instead of `new += ch`.
