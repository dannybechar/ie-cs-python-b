# Warm-up: this should build a new list of the temperatures below 21. It crashes. Read the
# error message, find the line, fix it.

temperature = [25, 20, 21, 24, 21, 24, 21, 16, 23]
new_list = []
for item in temperature:
    if item < 21:
        new_list.append(i)
print(new_list)


# Task 1: write colder_than(values, limit) - returns a NEW list with the values smaller than
# limit. Test on [25, 20, 21, 24, 21, 24, 21, 16, 23] with limit 21 and with limit 10.


# Task 2: write join_class(students, name) - if name is already in students, print
# "We cannot place you in this class" and return False; otherwise add it to the end of the list
# and return True. Test on ["Dana", "Avi", "Noa"] with "Avi" and with "Lior".


# Task 3: write all_palindromes(words) - returns True if EVERY word reads the same forwards and
# backwards, ignoring capital letters, otherwise False. Hint: a slice with step -1.
# Test on ["ABA", "1221", "A12321A"] (True) and ["ACA", "AcCA"] (also True) and ["ACA", "ACB"] (False).


# Task 4: write to_sentence(text) - turns "One#Apple#a#day#keeps#the#doctor#away" into a sentence
# with spaces (split, then join). Then write random_word(text) - returns one random word of the
# text (import random, random.choice). Run random_word three times.
