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


# Task 2: write name_check(names, name) - if name is in the list, print how many times it
# appears; if it is not, add it to the end of the list and print that it was added.
# Test on ["Dana", "Avi", "Dana", "Noa"] with "Dana", then "dana", then "Lior". Look at the list at the end.


# Task 3: write all_palindromes(words) - returns True if EVERY word reads the same forwards and
# backwards, ignoring capital letters, otherwise False. Hint: a slice with step -1.
# Test on ["ABA", "1221", "A12321A"] (True) and ["ACA", "AcCA"] (also True) and ["ACA", "ACB"] (False).


# Task 4 - the Sandwich challenge: write sandwich(text) - the text holds words separated by spaces.
# Return a NEW text with only the words whose first letter equals their last letter.
# You must use split and join. You may not use the + operator.
# "anna told bob he won level two!" -> "anna bob level"


# Task 5: a list is an "even list" when (a) its length is even and (b) its first half equals its second half.
# Write even_list(values) - returns True or False. Test on ["A", "b", "c", "A", "b", "c"] (True),
# [1, 2, 3] (False) and [1, 2, 3, 1, 2, 4] (False).


# If time (a): first and last names sit in one list in pairs (even cell = first name, odd cell = last name).
# Write same_initials(names) - how many pairs start with the same letter, ignoring capital letters?
# ["Amit", "Berkovich", "chen", "Cohen", "Daniel", "levi", "dana", "dikla", "Carmi", "Cohen"] -> 3


# If time (b): write to_sentence(text) - "One#Apple#a#day#keeps#the#doctor#away" becomes a sentence with spaces
# (split, then join). Then write random_word(text) - returns one random word (import random, random.choice).
