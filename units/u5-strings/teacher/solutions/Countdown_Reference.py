# Lessons 8.2–8.7 - countdown cases, reference for the teacher. No functions: the class has not learned def yet.
# Every case is solved twice, once with a for loop and once with a while loop, using a DIFFERENT idea.
# The countdown page is built from this file: each "# === case N for/while ===" section is run on every test
# value (the first line, text = ..., is replaced), and what it prints becomes the expected output.
# Cases (official exercises): 1 = worksheet 8.2 Q2, 2 = guided practice 8.4 task 1, 3 = deck 8.1 exercise 5,
# 4 = the enrichment video "new cipher" (not for the exam).


# === case 1 for ===
# walk over all the characters; the last one seen is the last character of the text
text = "Cats"
last = ""
for character in text:
    last = character
print(text[0] + "*" + last)

# === case 1 while ===
# compute the last place, len(text) - 1, and go straight to it
text = "Cats"
last_place = len(text) - 1
print(text[0] + "*" + text[last_place])

# === case 2 for ===
# compute the middle: len // 2, and % 2 tells odd from even
text = "robot"
half = len(text) // 2
if len(text) < 3:
    print(text)
elif len(text) % 2 == 1:
    print(text[half])
else:
    print(text[half - 1:half + 1])

# === case 2 while ===
# no arithmetic on the middle: a place at each end moves inward until one or two characters are left
text = "robot"
left = 0
right = len(text) - 1
while right - left > 1:
    left += 1
    right -= 1
print(text[left:right + 1])

# === case 3 for ===
# walk over the characters and remember the previous one in a variable
text = "American Standard Code Information Interchange"
result = ""
previous = " "
for character in text:
    if previous == " " and character != " ":
        result += character
    previous = character
print(result)

# === case 3 while ===
# walk over the places and look back at text[index - 1]
text = "American Standard Code Information Interchange"
result = text[0]
index = 1
while index < len(text):
    if text[index - 1] == " ":
        result += text[index]
    index += 1
print(result)

# === case 4 for ===
# isalpha() decides what is a letter; a letter becomes its number and a space, a space becomes 3 spaces
text = "Big Secret!"
result = ""
for character in text:
    if character.isalpha():
        result += str(ord(character)) + " "
    elif character == " ":
        result += "   "
    else:
        result += character
print(result)

# === case 4 while ===
# no isalpha(): a letter is an English letter only if its number is 65-90 (A-Z) or 97-122 (a-z)
text = "Big Secret!"
result = ""
index = 0
while index < len(text):
    number = ord(text[index])
    if 65 <= number <= 90 or 97 <= number <= 122:
        result += str(number) + " "
    elif text[index] == " ":
        result += "   "
    else:
        result += text[index]
    index += 1
print(result)
