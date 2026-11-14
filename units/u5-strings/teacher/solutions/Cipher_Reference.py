# Lessons 8.2–8.7 - reference for the teacher. No functions: the class has not learned def yet.
# Each task: a variable with the first test value, the code, and print. The whole file runs top to bottom;
# change a variable to try the other test values listed in its comment.


# Warm-up, explained: character == "a" or "e" or ... reads as (character == "a") or "e" or ...
# and a non-empty string such as "e" counts as True, so EVERY character is counted (19, the length).
# Fix: character in "aeiou"
text = "sometimes you learn"
total = 0
for character in text:
    if character in "aeiou":
        total += 1
print(total)                                   # 8

# Task 1: Ministry exercise 4 - first word and last word, no lists
text = "Cats and dogs are great friends"
first_space = text.find(" ")
if first_space == -1:
    print(text)
else:
    last_space = first_space
    for index in range(len(text)):
        if text[index] == " ":
            last_space = index
    print(text[:first_space] + " " + text[last_space + 1:])   # Cats friends   ("Hello" -> Hello)

# Task 2: Ministry exercise 5 - a word starts right after a space
text = "American Standard Code Information Interchange"
result = text[0]
for index in range(1, len(text)):
    if text[index - 1] == " ":
        result += text[index]
print(result)                                  # ASCII   ("hello big world" -> hbw)

# Task 3a: Ministry exercise 6 with count - "is" also hides inside "this" and "his"
text = "this is his list"
print(text.count("is"))                        # 4   ("mississippi" -> 2)

# Task 3b: the same without count - do the two characters that start at this place make "is"?
text = "this is his list"
total = 0
for index in range(len(text) - 1):
    if text[index:index + 2] == "is":
        total += 1
print(total)                                   # 4   ("mississippi" -> 2)

# Task 4a: Ministry exercise 7 with count
text = "sometimes you learn"
for vowel in "aeiou":
    print(vowel + ":", text.count(vowel))      # a: 1  e: 3  i: 1  o: 2  u: 1 (one per line)

# Task 4b: the same without count - one pass, five counters
text = "sometimes you learn"
a = 0
e = 0
i = 0
o = 0
u = 0
for character in text:
    if character == "a":
        a += 1
    elif character == "e":
        e += 1
    elif character == "i":
        i += 1
    elif character == "o":
        o += 1
    elif character == "u":
        u += 1
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)

# Task 5: ord and chr - the next-letter cipher (the Ministry's solution printed "a" on a line of its own;
# building a string with += and printing it once fixes that)
for character in "Hello":
    print(ord(character), end=",")
print()                                        # 72,101,108,108,111,
text = "abcd"
result = ""
for character in text:
    if character == "z":
        result += "a"
    elif character >= "a" and character < "z":
        result += chr(ord(character) + 1)
    else:
        result += character
print(result)                                  # bcde   ("zoo" -> app, "i like python" -> j mjlf qzuipo)

# Task 6: split and join - the list is only shown and printed here (lists come in lessons 9.1–14.5)
text = "guitar piano drums"
print(text.split(" "))                         # ['guitar', 'piano', 'drums']
print("-".join(text.split(" ")))               # guitar-piano-drums
print(text.replace(" ", "-"))                  # guitar-piano-drums - the same result

# Checkpoint 1: worksheet 8.2 question 3 - the middle letter; two letters when the length is even
word = "robot"
half = len(word) // 2
if len(word) % 2 == 1:
    print(word[half])
else:
    print(word[half - 1:half + 1])             # b   ("python" -> th, "a" -> a)

# Checkpoint 2: worksheet 8.2 question 4 - the first 4 and the last 4; **** when shorter than 4
text = "I like to play drums"
if len(text) < 4:
    print("****")
else:
    print(text[:4] + text[-4:])                # I lirums   ("abc" -> ****, "abcd" -> abcdabcd)

# Checkpoint 3: worksheet 8.2 question 7. Alternate by LETTER, not by index: the space must not count,
# so the index-parity hint in the worksheet would give TrUsT YoUrSeLf
text = "trust yourself"
result = ""
upper_next = True
for character in text:
    if character == " ":
        result += " "
    elif upper_next:
        result += character.upper()
        upper_next = False
    else:
        result += character.lower()
        upper_next = True
print(result)                                  # TrUsT yOuRsElF   ("ai" -> Ai)

# Enrichment - worksheet 8.2 questions 2, 5, 6, 8 (challenge)
# Q2: the first letter, a star, the last letter
text = "Cats and dogs are great friends"
print(text[0] + "*" + text[-1])                # C*s

# Q5: the last letter of every word: a letter is last when it is the end of the text or the next character is a space
text = "American Standard Code Information Interchange"
result = ""
for index in range(len(text)):
    if index == len(text) - 1 or text[index + 1] == " ":
        result += text[index]
print(result)                                  # ndene   ("I like to play drums" -> Ieoys)

# Q6: the WORD "it" - counting the characters "it" would also find the "it" inside "with" and "little"
text = "it is a little bit with it"
total = 0
word = ""
for character in text + " ":
    if character == " ":
        if word == "it":
            total += 1
        word = ""
    else:
        word += character
print(total)                                   # 2

# Q8 challenge: the second word and the word before the last (needs at least three words)
text = "Cats and dogs are great friends"
first_space = text.find(" ")
second_space = text.find(" ", first_space + 1)
second_word = text[first_space + 1:second_space]
last_space = -1
before_last_space = -1
for index in range(len(text)):
    if text[index] == " ":
        before_last_space = last_space
        last_space = index
print(second_word + " " + text[before_last_space + 1:last_space])   # and great
