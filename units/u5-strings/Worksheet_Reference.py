# Unit 5.4 - worksheet (countdown edition), reference for the teacher.
# One function per question; the expected values are printed at the bottom.


# Question 1, the bug explained: character == "a" or "e" or ... reads as (character == "a") or "e" or ...
# and a non-empty string such as "e" counts as True, so EVERY character is counted (19, the length).
# Fix: character in "aeiou"
def count_vowels(text):
    total = 0
    for character in text:
        if character in "aeiou":
            total += 1
    return total


# Question 2: the middle letter; two letters when the length is even (worksheet 8.2 Q3)
def middle(word):
    half = len(word) // 2
    if len(word) % 2 == 1:
        return word[half]
    return word[half - 1:half + 1]


# Question 3: the first 4 and the last 4 characters; "****" when the text is shorter than 4 (8.2 Q4)
def edges(text):
    if len(text) < 4:
        return "****"
    return text[:4] + text[-4:]


# Question 4: the last letter of every word (8.2 Q5): a letter is last when it is the end of the text
# or the next character is a space
def last_letters(text):
    result = ""
    for index in range(len(text)):
        if index == len(text) - 1 or text[index + 1] == " ":
            result += text[index]
    return result


# Question 5: letters alternate UPPER / lower; a space stays and does not count (8.2 Q7).
# Alternate by LETTER, not by index: index parity would give "TrUsT YoUrSeLf".
def alternate_case(text):
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
    return result


# If time: the WORD "it" (8.2 Q6) - counting the characters "it" would also find "with" and "little"
def count_word_it(text):
    total = 0
    word = ""
    for character in text + " ":
        if character == " ":
            if word == "it":
                total += 1
            word = ""
        else:
            word += character
    return total


print("Q1:", count_vowels("sometimes you learn"), "expected 8")
print("Q2:", middle("robot"), middle("python"), middle("a"), "expected b th a")
print("Q3:", edges("I like to play drums"), edges("abc"), edges("abcd"), "expected I lirums **** abcdabcd")
print("Q4:", last_letters("I like to play drums"), last_letters("Hello"), "expected Ieoys o")
print("Q5:", alternate_case("trust yourself"), alternate_case("ai"), "expected TrUsT yOuRsElF Ai")
print("If time:", count_word_it("it is a little bit with it"), "it" in "with", "expected 2 True")
