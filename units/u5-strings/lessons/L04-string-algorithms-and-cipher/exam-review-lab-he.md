# שיעורים 8.2-8.7 – מחרוזות: מעבדת סיכום (45 דקות)
שם: ______________________  תאריך: ______________
כותבים ביד בתיבה משמאל, מקלידים ב-Thonny ובודקים, מתקנים בצבע אחר ומגישים את הדף. כל שאלה עומדת בפני עצמה.
## שאלה 1: מצאו את הבאג
הקוד הבא אמור להדפיס את האות האחרונה ואת שלוש האותיות הראשונות, אבל הוא קורס. כתבו מה השגיאה, ותקנו שורה אחת.
```python
word = "keyboard"
print("Last:", word[len(word)])
print("First three:", word[0:3])
```
**כלים לשימוש:**
```python
len(word)    word[-1]
```
```text
Last: d
First three: key
```
## שאלה 2: כתובת מייל
נתונה כתובת מייל. הדפיסו את השם שלפני ה-@, את הדומיין שאחריו, את השם באותיות גדולות, ואם המילה school מופיעה בכתובת.
```python
email = "dana@school.org"
```
**כלים לשימוש:**
```python
email.find("@")
email[:place]    email[place + 1:]
.upper()    "school" in email
```
```text
Name: dana
Domain: school.org
Name in capitals: DANA
Has school: True
```
## שאלה 3: משפט
נתון משפט. הדפיסו כמה פעמים מופיעה המילה python (בלי קשר לגודל האותיות), החליפו את easy ב-great והדפיסו את המשפט החדש ואת האורך שלו.
```python
sentence = "Python is fun and Python is easy"
```
**כלים לשימוש:**
```python
sentence.lower()    .count("...")
sentence.replace("...", "...")
len(...)
```
```text
Python appears: 2
Changed: Python is fun and Python is great
New length: 33
```
## שאלה 4: בלי תנועות
נתון טקסט. ספרו כמה תנועות (a, e, i, o, u) יש בו, בלי קשר לגודל האותיות, ובנו טקסט חדש בלי התנועות. הרווחים נשארים.
```python
text = "Education is power"
```
**כלים לשימוש:**
```python
for ch in text:
ch.lower() in "aeiou"
rest += ch    count += 1
```
```text
Vowels: 8
Without vowels: dctn s pwr
```
## שאלה 5: שתי לולאות
נתונה מילה. ספרו בכמה מקומות אות זהה לאות שאחריה. אחר כך בנו, עם לולאה, מחרוזת מהאותיות שבמקומות הזוגיים (0, 2, 4...), והשוו אותה לחיתוך.
```python
word = "committee"
```
**כלים לשימוש:**
```python
for i in range(len(word) - 1):
word[i] == word[i + 1]
i % 2 == 0    word[::2]
```
```text
Doubles: 3
Loop: cmite
Slice: cmite
Same: True
```
