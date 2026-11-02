# Unit 5.4 - countdown cases, reference for the teacher. No functions: the class has not learned def yet.
# Every case is solved twice, once with a for loop and once with a while loop, using a DIFFERENT idea.
# The countdown page is built from this file: each "# === case N for/while ===" section is run on every test
# value (the first line, text = ..., is replaced), and what it prints becomes the expected output.


# === case 1 for ===
# check every place in the text: do the two characters that start there make "is"?
text = "this is his list"
total = 0
for index in range(len(text) - 1):
    if text[index:index + 2] == "is":
        total += 1
print(total)

# === case 1 while ===
# jump straight to the next "is" with find(..., start), until find says -1
text = "this is his list"
total = 0
place = text.find("is")
while place != -1:
    total += 1
    place = text.find("is", place + 1)
print(total)

# === case 2 for ===
# walk over the characters and remember the previous one in a variable
text = "American Standard Code Information Interchange"
result = ""
previous = " "
for character in text:
    if previous == " " and character != " ":
        result += character
    previous = character
print(result)

# === case 2 while ===
# walk over the places and look back at text[index - 1]
text = "American Standard Code Information Interchange"
result = text[0]
index = 1
while index < len(text):
    if text[index - 1] == " ":
        result += text[index]
    index += 1
print(result)

# === case 3 for ===
# a special case for "z"
text = "i like python"
result = ""
for character in text:
    if character == "z":
        result += "a"
    elif character.isalpha():
        result += chr(ord(character) + 1)
    else:
        result += character
print(result)

# === case 3 while ===
# no special case: the place in the alphabet (0-25), plus 1, and % 26 wraps 26 back to 0
text = "i like python"
result = ""
index = 0
while index < len(text):
    character = text[index]
    if character.isalpha():
        place = ord(character) - ord("a")
        place = (place + 1) % 26
        result += chr(ord("a") + place)
    else:
        result += character
    index += 1
print(result)

# === case 4 for ===
# walk over the whole text and remember the LAST space seen
text = "Cats and dogs are great friends"
first_space = text.find(" ")
if first_space == -1:
    print(text)
else:
    last_space = first_space
    for index in range(len(text)):
        if text[index] == " ":
            last_space = index
    first_word = text[:first_space]
    last_word = text[last_space + 1:]
    print(first_word + " " + last_word)

# === case 4 while ===
# start at the end and walk back until the first space you meet
text = "Cats and dogs are great friends"
first_space = text.find(" ")
if first_space == -1:
    print(text)
else:
    index = len(text) - 1
    while text[index] != " ":
        index -= 1
    first_word = text[:first_space]
    last_word = text[index + 1:]
    print(first_word + " " + last_word)
