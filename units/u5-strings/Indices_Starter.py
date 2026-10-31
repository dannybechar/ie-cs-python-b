# Warm-up: this should print the LAST letter of the word. Predict, run, read the error, then fix one expression.

word = "ROBOT"
last_letter = word[len(word)]
print(last_letter)


# Task 1 (predict first, on paper - then run and compare):
# What does each print show?
text1 = "I like to play, "
text2 = "piano"
text3 = "guitar"
print(text1 + text2)
print(text1 + text3)
print(text3 * 2)
msg1 = "abc" + "d" * 3
msg2 = "ef"
msg3 = "7"
print(msg1 + msg2)
print(len(msg1))
print(len(msg1 + msg2))
print(msg3 * 2)
print(len(msg3))


# Task 2: write two functions.
#   add_as_numbers(first, second)  - both parameters are strings of digits; return their SUM as a number
#   join_as_text(first, second)    - return the two strings joined into one string
# Test with "12" and "30": 42 for the first, "1230" for the second.


# Task 3: write show_edges(st). For the word "PYTHON" it must print, one per line,
#   the first letter twice (once with a positive index, once with a negative index),
#   the last letter twice, and the third letter twice (positive 2, negative -4).
# Test: show_edges("PYTHON")


# Task 4: write first_and_last(word) - return the first letter followed by the last letter.
# Test: "ROBOT" gives "RT"; "A" gives "AA".


# If time: write stars_for(word) - return as many "*" characters as the word has letters.
# Test: "hello" gives "*****".
