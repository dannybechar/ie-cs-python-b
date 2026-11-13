# Unit 5.4 - worksheet (countdown edition), reference for the teacher. No functions: the class has not learned def yet.
# Each question: a variable with the text, the code, and print. Change the value to try the other test values.


# Question 1, the bug explained: character == "a" or "e" or ... reads as (character == "a") or "e" or ...
# and a non-empty string such as "e" counts as True, so EVERY character is counted (19, the length).
# Fix: character in "aeiou"
text = "sometimes you learn"
total = 0
for character in text:
    if character in "aeiou":
        total += 1
print(total)                                   # 8

# Question 2: count the characters "is" without count (deck 8.1 exercise 6). Every place: do the two characters
# that start here make "is"? On the last place the slice is one character long (no crash) and never equals "is".
text = "this is his list"
total = 0
for index in range(len(text)):
    if text[index:index + 2] == "is":
        total += 1
print(total)                                   # 4   ("Mississippi" -> 2, "xyz" -> 0)

# Question 3: the first 4 and the last 4 characters; **** when the text is shorter than 4 (8.2 Q4)
text = "I like to play drums"
if len(text) < 4:
    print("****")
else:
    print(text[:4] + text[-4:])                # I lirums   ("abc" -> ****, "abcd" -> abcdabcd)

# Question 4: the last letter of every word (8.2 Q5): a letter is last when it is the end of the text
# or the next character is a space
text = "I like to play drums"
result = ""
for index in range(len(text)):
    if index == len(text) - 1 or text[index + 1] == " ":
        result += text[index]
print(result)                                  # Ieoys   ("Hello" -> o)

# Question 5: letters alternate UPPER / lower; a space stays and does not count (8.2 Q7).
# Alternate by LETTER, not by index: index parity would give TrUsT YoUrSeLf
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

# If time: the WORD "it" (8.2 Q6) - counting the characters "it" would also find "with" and "little"
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
