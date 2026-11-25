# Quiz Q1 (strings block) - full solutions, plain code, no functions.
print("=== Q1 a ===")
word = "pineapple"
print(word[2:5])
print(word[-4:])
print(word[::3])
print(word.find("app"))
print("pine" in word)
print(word.replace("p", "b"))
print("=== Q1 b ===")
a = "ice"
a + " cream"
print(a)

print("=== Q2 a (bug: IndexError) ===")
s = "hello"
for i in range(len(s)):
    print(s[i])
print("=== Q2 b (bug: count before lower) ===")
text = "Ana and ANA"
print(text.lower().count("ana"))

print("=== Q3 ===")
date = "25/11/2026"
print("Day:", date[:date.find("/")])
print("Year:", date[-4:])
print("With dashes:", date.replace("/", "-"))
print("Slashes:", date.count("/"))
print("Has 11:", "11" in date)

print("=== Q4 ===")
text = "Learn Strings Well"
count = 0
for ch in text:
    if ch.lower() == "l":
        count += 1
print("L count:", count)
rev = ""
for ch in text:
    rev = ch + rev
print("Reversed:", rev)
print("Same as slice:", rev == text[::-1])
for i in range(len(text)):
    if text[i].lower() == "l":
        print("Place:", i)
