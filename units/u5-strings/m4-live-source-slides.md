# Unit 5.4 live lesson slide content — 23 slides, 54 minutes

This deck is the frontal (knowledge) part of the meeting: the teacher presents one problem and builds the solution live, stage by stage, with the class. The rest of the meeting is the lab. Every slide has the footer "יחידה 5.4 – מחרוזות". Hebrew text is for the slides; code and program output stay exactly as written. A line starting with "Text:" is the wording for the slide.

Timers: only slides marked "Timer" show a timer (written "N דקות"). Other slides show no timer; their minutes are for the teacher.

### Slide 1 — יחידה 5.4 – מחרוזות

No timer on the slide (teacher time: 1 minute)

Title slide. Title: "יחידה 5.4 – מחרוזות". Subtitle: "מכונת הצופן הסודי".

### Slide 2 — הבעיה

No timer on the slide (teacher time: 5 minutes)

Text: "סוכן סודי שולח הודעה מוצפנת. התוכנית מקבלת הודעה והזזה, מצפינה, ובודקת שאפשר לפענח בחזרה. משתמשים בהודעות בדויות בלבד."
- הודעה באורך 5 תווים לפחות, והזזה בין 1 ל-25. אחרת שואלים שוב.
- אורך, מספר מילים (רווחים ועוד 1) והתו האמצעי.
- התו הראשון והאחרון, והמספר של כל אחד מהם.
- צופן הזזה: כל אות זזה קדימה, אחרי z חוזרים ל-a, והשאר לא משתנה.
- צופן מספרים וראשי תיבות.
- מסגרת סביב ההודעה המוצפנת.
- המקבל מקליד מילת קוד (ראשי התיבות), ומפענחים בחזרה ובודקים התאמה.

### Slide 3 — דוגמת הרצה: קלט וקודים

No timer on the slide (teacher time: 1 minute)

```text
Message: hi
Too short, try again
Message: Meet at old bridge
Shift (1-25): 30
Shift must be 1 to 25
Shift (1-25): 3
Length: 18
Words: 4
Middle: ol
First: M 77
Last: e 101
Next after first: N
```

### Slide 4 — דוגמת הרצה: הצפנה ופענוח

No timer on the slide (teacher time: 1 minute)

```text
Coded: Phhw dw rog eulgjh
Numbers: 77 101 101 116 32 97 116 32 111 108 100 32 98 114 105 100 103 101 
Initials: Maob
**********************
* Phhw dw rog eulgjh *
**********************
Dashes: Phhw-dw-rog-eulgjh
Code word: xyz
Wrong code word
Code word: maob
Decoded: Meet at old bridge
Match: yes
```
- שאלה לכיתה: איך תו הופך למספר, ואיך מספר חוזר להיות תו?

### Slide 5 — שישה שלבים

No timer on the slide (teacher time: 2 minutes)

Table (keep column order):

| שלב | מה מוסיפים | מה לומדים |
|---|---|---|
| 1 | בדיקות קלט ועובדות על ההודעה | `while`, `count(" ") + 1`, תו אמצעי |
| 2 | אותיות הן מספרים | `ord`, `chr` |
| 3 | צופן הזזה | `for ch in text`, `isalpha`, `+=` |
| 4 | צופן מספרים וראשי תיבות | בנייה עם `+=` ו-`range(1, len)` |
| 5 | דוח: מסגרת | `"*" * n`, `split` ו-`join` (רק מראים) |
| 6 | המקבל: מילת קוד ופענוח | `while` על קלט, פענוח הפוך |

### Slide 6 — אותיות הן מספרים

No timer on the slide (teacher time: 3 minutes)

```python
print(ord("a"))
print(ord("b"))
print(chr(100))
print(chr(ord("a") + 3))
print(ord("A"))
```
```text
97
98
d
d
65
```
- `ord` נותנת את המספר של תו אחד. `chr` נותנת את התו של מספר.
- אותיות קטנות הן 97 עד 122. אותיות גדולות הן 65 עד 90.
- הזזה של אות היא חיבור על המספר שלה.

### Slide 7 — חוזים: מספרים ותווים

Timer on the slide: **3 דקות**

```python
print(ord("a"))
print(ord("A"))
print(chr(100))
print(chr(ord("c") + 1))
print(ord("0"))
```
Text: "חזו על הנייר את חמש שורות הפלט."
QUESTION ONLY: do not show the output.

### Slide 8 — חוזים: התשובה

No timer on the slide (teacher time: 1 minute)

```text
97
65
d
d
48
```
- אות גדולה וקטנה הן מספרים שונים, ולכן הן תווים שונים.
- `"0"` הוא תו, והמספר שלו הוא 48, לא 0.

### Slide 9 — שלב 1: בדיקות קלט

No timer on the slide (teacher time: 2 minutes)

```python
message = input("Message: ")
while len(message) < 5:
    print("Too short, try again")
    message = input("Message: ")
shift = int(input("Shift (1-25): "))
while shift < 1 or shift > 25:
    print("Shift must be 1 to 25")
    shift = int(input("Shift (1-25): "))
```
```text
Message: hi
Too short, try again
Message: Meet at old bridge
Shift (1-25): 30
Shift must be 1 to 25
Shift (1-25): 3
```
- למה `or` ולא `and` בתנאי של ההזזה?

### Slide 10 — שלב 1: עובדות על ההודעה

No timer on the slide (teacher time: 2 minutes)

```python
size = len(message)
words = message.count(" ") + 1
if size % 2 == 1:
    middle = message[size // 2]
else:
    middle = message[size // 2 - 1:size // 2 + 1]
print("Length:", size)
print("Words:", words)
print("Middle:", middle)
```
```text
Length: 18
Words: 4
Middle: ol
```
- למה מספר המילים הוא מספר הרווחים ועוד 1?
- למה באורך זוגי יש שני תווים באמצע?

### Slide 11 — שלב 2: הראשון והאחרון

No timer on the slide (teacher time: 3 minutes)

```python
first = message[0]
last = message[-1]
print("First:", first, ord(first))
print("Last:", last, ord(last))
print("Next after first:", chr(ord(first) + 1))
```
```text
First: M 77
Last: e 101
Next after first: N
```
- מה עושה `chr(ord(first) + 1)`, צעד אחר צעד?
- מה יקרה אם התו הראשון הוא `z`?

### Slide 12 — חוזים: לולאה והזזה

Timer on the slide: **3 דקות**

```python
word = "abz"
out = ""
for ch in word:
    out += chr(ord(ch) + 1)
print(out)
```
Text: "מה יודפס? כתבו על הנייר."
QUESTION ONLY: do not show the output.

### Slide 13 — חוזים: התשובה

No timer on the slide (teacher time: 1 minute)

```text
bc{
```
- אחרי `z` בא הסימן `{`, לא `a`. צריך לחזור להתחלה.
- הבעיה הזאת היא הסיבה לשורה `code -= 26` בשלב הבא.

### Slide 14 — שלב 3: צופן הזזה

No timer on the slide (teacher time: 5 minutes)

```python
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
print("Coded:", coded)
```
```text
Coded: Phhw dw rog eulgjh
```
- למה רווח לא עובר הזזה?
- למה משווים ל-`ord("z")` באות קטנה ול-`ord("Z")` באות גדולה?

### Slide 15 — שלב 4: צופן מספרים וראשי תיבות

No timer on the slide (teacher time: 4 minutes)

```python
numbers = ""
for ch in message:
    numbers += str(ord(ch)) + " "
initials = message[0]
for index in range(1, size):
    if message[index - 1] == " ":
        initials += message[index]
print("Numbers:", numbers)
print("Initials:", initials)
```
```text
Numbers: 77 101 101 116 32 97 116 32 111 108 100 32 98 114 105 100 103 101 
Initials: Maob
```
- למה צריך `str(...)` לפני `+`?
- למה הלולאה של ראשי התיבות מתחילה מ-1?

### Slide 16 — split ו-join: רק מראים

No timer on the slide (teacher time: 3 minutes)

```python
text = "red blue green"
print(text.split(" "))
print("-".join(text.split(" ")))
print(text)
```
```text
['red', 'blue', 'green']
red-blue-green
red blue green
```
- `split(" ")` חותכת במקום הרווחים. `join` מדביקה בחזרה עם מה שבין המרכאות.
- התוצאה של `split` היא רשימה. היא נלמדת ביחידה 7, ולכן רק מדפיסים ומדביקים.
- המחרוזת המקורית לא השתנתה.

### Slide 17 — שלב 5: דוח עם מסגרת

No timer on the slide (teacher time: 3 minutes)

```python
line = "*" * (len(coded) + 4)
print(line)
print("*", coded, "*")
print(line)
print("Dashes:", "-".join(coded.split(" ")))
```
```text
**********************
* Phhw dw rog eulgjh *
**********************
Dashes: Phhw-dw-rog-eulgjh
```
- למה המסגרת ארוכה ב-4 תווים מההודעה?

### Slide 18 — שלב 6: מילת קוד

No timer on the slide (teacher time: 1 minute)

```python
code_word = input("Code word: ")
while code_word.lower() != initials.lower():
    print("Wrong code word")
    code_word = input("Code word: ")
```
```text
Code word: xyz
Wrong code word
Code word: maob
```
- למה משווים את מילת הקוד באותיות קטנות?

### Slide 19 — שלב 6: המקבל מפענח

No timer on the slide (teacher time: 3 minutes)

```python
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
print("Decoded:", decoded)
if decoded == message:
    print("Match: yes")
else:
    print("Match: no")
```
```text
Decoded: Meet at old bridge
Match: yes
```
- איך הפענוח הפוך להצפנה?

### Slide 20 — שגיאות שכדאי להכיר

No timer on the slide (teacher time: 2 minutes)

Wrong use:
```python
print(ord("ab"))
```
```text
TypeError: ord() expected a character, but string of length 2 found
```
Wrong use:
```python
print(chr(ord("Z") + 1))
```
```text
[
```
- `ord` מקבלת תו אחד בלבד.
- שגיאה שקטה: אחרי `Z` לא בא `A`, אלא `[`. התוכנית רצה ונותנת תשובה שגויה.
- `"Age " + ord("a")` נותנת `TypeError`: צריך `str(ord("a"))`.

### Slide 21 — מה למדנו

No timer on the slide (teacher time: 2 minutes)

Table (keep column order):

| כלי | מה הוא עושה | דוגמה |
|---|---|---|
| `ord` | המספר של תו | `ord("a")` |
| `chr` | התו של מספר | `chr(97)` |
| `count(" ") + 1` | מספר המילים | `"a b c".count(" ") + 1` |
| `"*" * n` | מסגרת | `"*" * 5` |
| `split` ו-`join` | רק מראים | `"-".join(text.split(" "))` |
| `+=` | בונים מחרוזת | `coded += chr(code)` |

### Slide 22 — בדיקת יציאה

Timer on the slide: **2 דקות**

```python
text = "Hi Bob"
```
Text: "מה הערך?"
1. `ord(text[0])`
2. `chr(ord("b") + 1)`
3. `text.count(" ") + 1`
4. `chr(ord(text[-1]) - 1)`

QUESTION ONLY: do not show the answers.

### Slide 23 — בדיקת יציאה: התשובות

No timer on the slide (teacher time: 1 minute)

```text
ord(text[0])                 72
chr(ord("b") + 1)            c
text.count(" ") + 1          2
chr(ord(text[-1]) - 1)       a
```
- `H` היא אות גדולה, ולכן 72 ולא 104.
- התו האחרון הוא `b`, ואחד לפניו באלף-בית הוא `a`.
