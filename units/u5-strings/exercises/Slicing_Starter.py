# Warm-up: this should print the title in capital letters, but it still prints it in lower case. Predict, run, then fix ONE line.
# Tasks 1-4: write your code under each variable and print the answer. Run, check, then change the value and run again.

title = "strings are sequences"
title.upper()
print(title)


# Task 1: write the slice that prints each wanted output. Test every line.
text = "I like to play drums"
#   wanted "drums"       -> print(text[...])
#   wanted "to play"     -> print(text[...])
#   wanted "Ikoar"       -> print(text[...])
number = "345124987"     # a STRING of digits, not a number
#   wanted "124"         -> print(number[...])
#   wanted "49"          -> print(number[...])
#   wanted "4512"        -> print(number[...])
#   wanted "987"         -> print(number[...])


# Task 2: print how many times the characters "the" appear in text.
# "the other theme is there" prints 4. Then print "aaaa".count("aa") and explain what you see.
text = "the other theme is there"



# Task 3: replace the character | with the two letters we, only in the first three places where it appears,
# and print the new string. "a|b|c|d|e" prints awebwecwed|e
text = "a|b|c|d|e"



# Task 4: print True when text contains yes in any letter case (yes, YES, Yes ...), otherwise False.
# "Maybe YES maybe no" prints True, then try "no way" - it prints False.
text = "Maybe YES maybe no"



# If time: print True when address contains "@" and, after the "@", it also contains a "."
# (use find with a start position). "dana@school.org" True, then try "dana@school" False, "dana.school" False.
address = "dana@school.org"

