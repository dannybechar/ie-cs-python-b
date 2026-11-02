# Unit 5.3 - reference for the teacher. No functions: the class has not learned def yet.
# Each task: a variable with the text, the code, and print. Change the value to try the other test values.
# Task 4 reads 6 surnames (3 for version a, 3 for version b) - type them, or pipe them in.


# Warm-up, explained: count = 0 sits INSIDE the loop, so the counter restarts from zero for every character
# and the print shows the answer for the LAST character only ("n" -> 0). It must be set once, before the loop.
text = "sometimes you win sometimes you learn"
letter = "e"
count = 0
for character in text:
    if character == letter:
        count += 1
print(count)                                   # 5

# Task 1: isdigit + len (worksheet 7.2, questions 12 and 14 first, as a predict-and-check)
text = "I like to play drums"
print(text.startswith("I like"))               # True
print(text.startswith("play", 10, 17))         # True
print(text.startswith("to play", 10, 17))      # False - text[10:17] is "play dr"

text = "2027"
print(text.isdigit() and len(text) == 4)       # True   ("1.9.2027", "20x7", "99" -> False)

# Task 2: count with a for loop, no count() (Ministry exercise 1); print once, after the loop
text = "sometimes you win sometimes you learn"
letter = "e"
count = 0
for character in text:
    if character == letter:
        count += 1
print(count)                                   # 5   ("banana" / "a" -> 3, "banana" / "z" -> 0)

# Task 3: (a) print with end="" (Ministry exercise 2), (b) build the same string with += and print it once
text = "Learn"
for character in text:
    print(character * 3, end="")
print()                                        # LLLeeeaaarrrnnn

result = ""
for character in text:
    result += character * 3
print(result)                                  # LLLeeeaaarrrnnn   ("ab" -> aaabbb)

# Task 4: Ministry exercise 3 - reads the surnames itself (type them, or pipe them in)
# Version a: with count
number = 3
total = 0
for turn in range(number):
    surname = input("Surname: ").lower()
    if surname.count("cohen") > 0:
        total += 1
print(total)                                   # Cohen, Levi, BenCOHEN -> 2

# Version b: without count - use in
number = 3
total = 0
for turn in range(number):
    surname = input("Surname: ").lower()
    if "cohen" in surname:
        total += 1
print(total)                                   # Cohen, Levi, BenCOHEN -> 2

# Task 5: build a new string from selected characters (the code on the Ministry slide)
text = "We play on the computer"
result = ""
for character in text:
    if character >= "a" and character <= "e":
        result += character
print(result)                                  # eaece   ("abcdefg" -> abcde)

# If time: spaces + 1 = words, as long as every gap is a single space
text = "We are learning to program"
spaces = 0
for character in text:
    if character == " ":
        spaces += 1
print(spaces + 1)                              # 5   ("two  spaces" -> 3, not 2: a gap of two spaces counts twice)
