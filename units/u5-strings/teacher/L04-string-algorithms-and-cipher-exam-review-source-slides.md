# Lessons 8.2–8.7 exam-review deck — 5 slides, 45 minutes

Closing deck of the strings block. It covers exactly the strings topics of the Ministry's מיקוד for the mafmar (chapter 5): the empty string, `+` and `*`, `in`, indexing and slicing `[]` `[::]`, `len` `find` `upper` `lower` `count` `replace`, and the two bounded loops (`for ch in st` and `for i in range(len(st))`). It leaves out everything the מיקוד marks as not examined (`startswith`, `endswith`, `isalpha`, `isnumeric`) and the optional Ministry extras (`ord`, `chr`, `split`, `join`). Every slide is a content part plus complete code the teacher copies into Thonny. Build: `python tools/live-deck/build_deck.py <this file> deck.html --footer "שיעורים 8.2–8.7 – מחרוזות" --no-title`.

No timers on the slides; the teacher time is noted per slide and sums to 45 minutes. The paper lab (45 minutes) follows.

### Slide 1 — מה במבחן: פעולות על מחרוזות

No timer on the slide (teacher time: 9 minutes)

- מחרוזת ריקה: `""`. האורך שלה 0.
- חיבור וחזרה: `"gu" + "itar"` ו-`"ha" * 3`.
- האם מופיע: `"tar" in word` נותן `True` או `False`.
- תו במקום: `word[0]`, `word[-1]`. חיתוך: `word[1:4]`, `word[::-1]`.
- מחרוזת היא רצף תווים, וכל תו יושב במקום שמתחיל ב-0.
- שאלה: מה האורך של מחרוזת ריקה, ומה `"ha" * 0`?
```python
word = "guitar"
print(word + "s")
print(word * 2)
print("tar" in word)
print(len(""))
```
```text
guitars
guitarguitar
True
0
```

### Slide 2 — אינדקס וחיתוך

No timer on the slide (teacher time: 9 minutes)

- `word[i]` תו אחד. `-1` הוא האחרון. מקום שלא קיים נותן שגיאה.
- `word[a:b]` מהמקום a ועד לפני b. אפשר להשמיט a (מההתחלה) או b (עד הסוף).
- `word[::2]` כל תו שני. `word[::-1]` הפוך.
- חיתוך לא נותן שגיאה גם אם הקצה רחוק. מראים ב-Thonny: `word[6]`.
- שאלה: מה מדפיס `word[3:3]`?
```python
word = "guitar"
print(word[0], word[-1])
print(word[1:4])
print(word[:3])
print(word[2:])
print(word[::2])
print(word[::-1])
```
```text
g r
uit
gui
itar
gia
ratiug
```

### Slide 3 — פעולות מרכזיות

No timer on the slide (teacher time: 9 minutes)

- `len(s)` מספר התווים. `s.count(x)` כמה פעמים x מופיע.
- `s.find(x)` המקום הראשון של x, או -1 אם אין.
- `s.upper()` ו-`s.lower()` עותק באותיות גדולות או קטנות.
- `s.replace(a, b)` עותק שבו a הוחלף ב-b.
- מחרוזת לא משתנה. הפעולות מחזירות מחרוזת חדשה, ולכן צריך `print` או משתנה.
- שאלה: אחרי `song.replace(" ", "_")`, מה תהיה `song`?
```python
song = "Let It Be"
print(len(song))
print(song.upper())
print(song.find("It"))
print(song.find("z"))
print(song.lower().count("t"))
print(song.replace(" ", "_"))
print(song)
```
```text
9
LET IT BE
4
-1
2
Let_It_Be
Let It Be
```

### Slide 4 — שתי לולאות: על התוכן ועל המקום

No timer on the slide (teacher time: 9 minutes)

- `for ch in text:` רק התווים: ספירה, בדיקה, `+=`.
- `for i in range(len(text)):` המקום חשוב: שכן, דילוג.
- שאלה: למה בבדיקת שכן כתוב `len(word) - 1`?
```python
text = "cat"
for ch in text:
    print(ch)
for i in range(len(text)):
    print(i, text[i])
```
```text
c
a
t
0 c
1 a
2 t
```
```python
word = "balloon"
doubles = 0
for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
        doubles += 1
print(doubles)
```
```text
2
```

### Slide 5 — תוכנית אחת שמחברת הכול

No timer on the slide (teacher time: 9 minutes)

- הבעיה: אורך, אותיות גדולות, הפוך, מקפים במקום רווחים, האם יש `ai`, כמה `e` ובאילו מקומות.
- שאלה: למה הבדיקה והספירה על `low` ולא על `text`?
```python
text = input("Text: ")
low = text.lower()
print("Length:", len(text))
print("Upper:", text.upper())
print("Reversed:", text[::-1])
print("Dashes:", text.replace(" ", "-"))
if "ai" in low:
    print("AI found")
count = 0
for ch in low:
    if ch == "e":
        count += 1
print("E count:", count)
for i in range(len(low)):
    if low[i] == "e":
        print("e at", i)
```
```text
Text: Learn AI With Me
Length: 16
Upper: LEARN AI WITH ME
Reversed: eM htiW IA nraeL
Dashes: Learn-AI-With-Me
AI found
E count: 2
e at 1
e at 15
```
