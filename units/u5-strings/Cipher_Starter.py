# Warm-up: count_vowels should count only a, e, i, o and u - but it counts every character. Predict, run, then fix ONE line.

def count_vowels(text):
    total = 0
    for character in text:
        if character == "a" or "e" or "i" or "o" or "u":
            total += 1
    return total


print(count_vowels("sometimes you learn"))   # should be 8


# Task 1: write first_and_last_word(text) - return the first word and the last word with one space between them.
# Test: "Cats and dogs are great friends" gives "Cats friends".  Hint: find(" ") for the first space; a loop remembers the last one.


# Task 2: write initials(text) - return the first letters of all the words.
# Test: "American Standard Code Information Interchange" gives "ASCII".  Hint: a word starts right after a space (and at index 0).


# Task 3: write count_is_a(text) using count(), and count_is_b(text) WITHOUT count() - how many times "is" appears.
# Test: "this is his list" gives 4. (Why is it not 1?)


# Task 4: write print_vowels(text) - print how many a, e, i, o and u the text has, one letter per line like "a: 3".
# Without count(): one pass over the text and five counters.


# Task 5 (first run this and read the numbers:  for ch in "Hello": print(ord(ch), end=","))
# Write next_letters(text) - return a text where every letter is replaced by the next letter in the alphabet,
# and "z" becomes "a". Other characters (spaces) stay as they are. Lower-case only.
# Test: "abcd" gives "bcde", "zoo" gives "app", "i like python" gives "j mjlf qzuipo".


# Task 6: split and join - run and read, nothing to write yet:
#   text = "guitar piano drums"
#   print(text.split(" "))
#   print("-".join(text.split(" ")))
# Then write dash_words(text) - the text with every space replaced by "-", using split and join. Compare with replace.


# CHECKPOINT - write these three functions on your own:
#   middle(word)          - return the middle letter; if the word has an even number of letters, the two middle letters.
#                           "robot" -> "b", "python" -> "th"
#   edges(text)           - return the first 4 characters followed by the last 4; if the text has fewer than 4 characters,
#                           return "****".   "I like to play drums" -> "I lirums"
#   alternate_case(text)  - letters alternate UPPER, lower, UPPER ...; a space stays and does not count as a letter.
#                           "trust yourself" -> "TrUsT yOuRsElF"
# Homework / enrichment: worksheet 8.2, questions 2, 5, 6 and the challenge 8.
