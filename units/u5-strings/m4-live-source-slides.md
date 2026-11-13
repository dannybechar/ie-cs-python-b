# Unit 5.4 live lesson slide content — 10 slides, 54 minutes (five pairs)

Compact deck for the frontal part of the meeting. It starts directly with the content (no title slide, no problem slides). It is built as five pairs: a **content slide** followed by a **code-examples slide**. The teacher goes from the slide to Thonny, copies each example from the slide, runs it, and shows the result. Every code example is complete and runs on its own (fixed strings, no `def`). Every slide has the footer "יחידה 5.4 – מחרוזות". Hebrew text is for the slides; code and program output stay exactly as written. Build: `python tools/live-deck/build_deck.py m4-live-source-slides.md deck.html --footer "יחידה 5.4 – מחרוזות" --no-title`.

No timers on slides; the minutes are for the teacher (content slide 3 + code slide 8 = 11 per pair; the last pair is 10; 54 minutes in all).

### Slide 1 — אותיות הן מספרים

No timer on the slide (teacher time: 3 minutes)

| כלי | מה הוא עושה | דוגמה |
|---|---|---|
| `ord` | המספר של תו אחד | `ord("a")` |
| `chr` | התו של מספר | `chr(97)` |
- אותיות קטנות הן 97 עד 122. אותיות גדולות הן 65 עד 90. התו `"0"` הוא 48.
- הזזה של אות היא חיבור על המספר שלה.
- שאלה: מה בא אחרי `z`, אם מוסיפים 1 למספר שלה?
### Slide 2 — קוד להרצה: ord ו-chr

No timer on the slide (teacher time: 8 minutes)

```python
print(ord("a"))
print(ord("A"))
print(ord("0"))
```
```text
97
65
48
```
```python
print(chr(100))
print(chr(ord("a") + 3))
print(chr(ord("z") + 1))
```
```text
d
d
{
```
```python
word = "abz"
out = ""
for ch in word:
    out += chr(ord(ch) + 1)
print(out)
```
```text
bc{
```

### Slide 3 — בדיקות ועובדות על ההודעה

No timer on the slide (teacher time: 3 minutes)

- `while` שואלת שוב כל עוד הקלט לא תקין: `while len(message) < 5`.
- אורך: `len(message)`. מספר מילים: מספר הרווחים ועוד 1.
- התו הראשון `message[0]`, האחרון `message[-1]`.
- אורך אי-זוגי: תו אחד באמצע. אורך זוגי: שני תווים באמצע (חיתוך).
- שאלה: למה באורך זוגי יש שני תווים באמצע?
### Slide 4 — קוד להרצה: בדיקות ועובדות

No timer on the slide (teacher time: 8 minutes)

```python
message = input("Message: ")
while len(message) < 5:
    print("Too short, try again")
    message = input("Message: ")
print("OK:", message)
```
```text
Message: hi
Too short, try again
Message: Meet at old bridge
OK: Meet at old bridge
```
```python
message = "Meet at old bridge"
size = len(message)
print(size)
print(message.count(" ") + 1)
print(message[0], message[-1])
half = size // 2
if size % 2 == 1:
    middle = message[half]
else:
    middle = message[half-1:half+1]
print(middle)
```
```text
18
4
M e
ol
```

### Slide 5 — צופן הזזה

No timer on the slide (teacher time: 3 minutes)

- עוברים על ההודעה עם `for ch in message` ובונים מחרוזת חדשה עם `+=`.
- רק אותיות זזות: `ch.isalpha()`. רווח וסימנים מועתקים כמו שהם.
- `code = ord(ch) + shift`. אחרי `z` (או `Z`) חוזרים להתחלה: `code -= 26`.
- לאות קטנה הסוף הוא `ord("z")`, לאות גדולה `ord("Z")`.
- דוגמה: `x` זזה 3 מקומות ונהיית `a`. שאלה: מה יקרה אם נשכח את `code -= 26`?
### Slide 6 — קוד להרצה: צופן הזזה

No timer on the slide (teacher time: 8 minutes)

```python
message = "Meet at old bridge"
shift = 3
coded = ""
for ch in message:
    if ch.isalpha():
        code = ord(ch) + shift
        if ch == ch.lower():
            end = ord("z")
        else:
            end = ord("Z")
        if code > end:
            code -= 26
        coded += chr(code)
    else:
        coded += ch
print(coded)
```
```text
Phhw dw rog eulgjh
```

### Slide 7 — מספרים, ראשי תיבות ומסגרת

No timer on the slide (teacher time: 3 minutes)

- צופן מספרים: `str(ord(ch)) + " "`. צריך `str` לפני `+`.
- ראשי תיבות: התו הראשון, ועוד כל תו שבא אחרי רווח. הלולאה מתחילה מ-1 כי בודקים `message[i - 1]`.
- מסגרת: `"*" * n`. אורך המסגרת הוא אורך ההודעה ועוד 4.
- `split` ו-`join`: רק מראים. התוצאה של `split` היא רשימה, ורשימות נלמדות ביחידה 7.
- שאלה: למה המסגרת ארוכה ב-4 תווים מההודעה?
### Slide 8 — קוד להרצה: מספרים, ראשי תיבות ומסגרת

No timer on the slide (teacher time: 8 minutes)

```python
message = "Meet at"
numbers = ""
for ch in message:
    numbers += str(ord(ch)) + " "
print(numbers)
initials = message[0]
for i in range(1, len(message)):
    if message[i - 1] == " ":
        initials += message[i]
print(initials)
```
```text
77 101 101 116 32 97 116 
Ma
```
```python
coded = "Phhw dw rog eulgjh"
line = "*" * (len(coded) + 4)
print(line)
print("*", coded, "*")
print(line)
print("-".join(coded.split(" ")))
```
```text
**********************
* Phhw dw rog eulgjh *
**********************
Phhw-dw-rog-eulgjh
```

### Slide 9 — פענוח ומילת קוד

No timer on the slide (teacher time: 3 minutes)

- פענוח הוא ההפך: `ord(ch) - shift`, ואם יצאנו לפני `a` מוסיפים 26.
- בדיקה: `decoded == message` מחזיר `True` כשהפענוח הצליח. `"MAOB".lower() == "maob"` מחזיר `True`.
- מילת קוד: `while` על קלט (כמו בבדיקת ההודעה), והשוואה באותיות קטנות עם `lower()`.
- `ord("ab")` נותנת `TypeError`: `ord` מקבלת תו אחד בלבד.
- אחרי `Z` בא `[` ולא `A`: שגיאה שקטה, התוכנית רצה ונותנת תשובה שגויה.
### Slide 10 — קוד להרצה: פענוח ומילת קוד

No timer on the slide (teacher time: 7 minutes)

```python
coded = "Phhw dw rog eulgjh"
message = "Meet at old bridge"
shift = 3
decoded = ""
for ch in coded:
    if ch.isalpha():
        code = ord(ch) - shift
        if ch == ch.lower():
            start = ord("a")
        else:
            start = ord("A")
        if code < start:
            code += 26
        decoded += chr(code)
    else:
        decoded += ch
print(decoded)
print(decoded == message)
```
```text
Meet at old bridge
True
```
