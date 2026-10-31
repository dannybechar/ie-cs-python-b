# Warm-up: this should print the title in capital letters, but it still prints it in lower case. Predict, run, then fix ONE line.

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


# Task 2: write count_the(text) - return how many times the characters "the" appear in text.
# Test: "the other theme is there" gives 4. Then check what count("aa") gives on "aaaa" and explain it.


# Task 3: write replace_first_three(text) - replace the character | with the two letters we,
# only in the first three places where it appears. Return the new string.
# Test: "a|b|c|d|e" gives "awebwecwed|e"


# Task 4: write has_yes(text) - return True when text contains yes in any letter case (yes, YES, Yes ...).
# Test: "Maybe YES maybe no" gives True, "no way" gives False.


# If time: write looks_like_email(address) - return True when the text contains "@" and, after the "@",
# it also contains a "." (use find with a start position). Test: "dana@school.org" True, "dana@school" False,
# "dana.school" False.
