# Unit 5.2 - reference for the teacher. No functions: the class has not learned def yet.
# Each task: a variable, the code, and print. Change the value to try the other test values.


# Warm-up, explained: upper() gives back a NEW string and the program threw it away. Fix: title = title.upper()
title = "strings are sequences"
title = title.upper()
print(title)                                   # STRINGS ARE SEQUENCES

# Task 1: write the slice for each wanted output (worksheet 7.2, questions 5-6)
text = "I like to play drums"
print(text[-5:])       # drums
print(text[7:14])      # to play
print(text[::4])       # Ikoar
number = "345124987"
print(number[3:6])     # 124
print(number[-4:-2])   # 49
print(number[1:5])     # 4512
print(number[6:])      # 987

# Task 2: count (worksheet question 15). count never counts overlapping matches.
text = "the other theme is there"
print(text.count("the"))                       # 4
print("aaaa".count("aa"))                      # 2, not 3

# Task 3: replace with a count (worksheet question 9) - a new string comes back
text = "a|b|c|d|e"
print(text.replace("|", "we", 3))              # awebwecwed|e

# Task 4: normalize with lower() before checking "in" (worksheet question 13)
text = "Maybe YES maybe no"
print("yes" in text.lower())                   # True   ("no way" -> False)

# If time: find with a start position - the "." must come after the "@"
address = "dana@school.org"
at = address.find("@")
if at == -1:
    print(False)
else:
    print(address.find(".", at + 1) != -1)     # True   ("dana@school" -> False, "dana.school" -> False)
