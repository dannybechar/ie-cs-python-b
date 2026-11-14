# Warm-up: this code should count only a, e, i, o and u - but it counts every character. Predict, run, then fix ONE line.
# Tasks: write your code under each variable, ending with print. Run, compare with the comment, then change the value and run again.
# Tip: while you work on one task, put a # before the code of the others (in Thonny: select the lines, Ctrl+3).

text = "sometimes you learn"
total = 0
for character in text:
    if character == "a" or "e" or "i" or "o" or "u":
        total += 1
print(total)                                   # should be 8


# Task 1: print the first word and the last word with one space between them.
# Test: "Cats and dogs are great friends" prints Cats friends; "Hello" prints Hello.
# Hint: find(" ") for the first space; a loop remembers the last one.
text = "Cats and dogs are great friends"



# Task 2: print the first letters of all the words.
# Test: "American Standard Code Information Interchange" prints ASCII; "hello big world" prints hbw.
# Hint: a word starts right after a space (and at index 0).
text = "American Standard Code Information Interchange"



# Task 3a: print how many times "is" appears, using count().
# Test: "this is his list" prints 4 (why is it not 1?); "mississippi" prints 2.
text = "this is his list"



# Task 3b: the same WITHOUT count().
text = "this is his list"



# Task 4a: print how many a, e, i, o and u the text has, one letter per line like "a: 1" - using count().
# Test: "sometimes you learn" prints a: 1, e: 3, i: 1, o: 2, u: 1 (on five lines).
text = "sometimes you learn"



# Task 4b: the same WITHOUT count(): one pass over the text and five counters.
text = "sometimes you learn"



# Task 5 (first run this and read the numbers:  for ch in "Hello": print(ord(ch), end=","))
# Print the text with every letter replaced by the next letter in the alphabet; "z" becomes "a".
# Other characters (spaces) stay as they are. Lower-case only.
# Test: "abcd" prints bcde, "zoo" prints app, "i like python" prints j mjlf qzuipo.
text = "abcd"



# Task 6: split and join - run and read, nothing to write yet:
#   print(text.split(" "))
#   print("-".join(text.split(" ")))
# Then print the text with every space replaced by "-", using split and join. Compare with replace.
text = "guitar piano drums"



# CHECKPOINT - write these three on your own:
# Checkpoint 1: print the middle letter; if the word has an even number of letters, the two middle letters.
# Test: "robot" prints b, "python" prints th, "a" prints a.
word = "robot"



# Checkpoint 2: print the first 4 characters followed by the last 4; if the text has fewer than 4 characters,
# print ****.   Test: "I like to play drums" prints I lirums, "abc" prints ****.
text = "I like to play drums"



# Checkpoint 3: letters alternate UPPER, lower, UPPER ...; a space stays and does not count as a letter.
# Test: "trust yourself" prints TrUsT yOuRsElF.
text = "trust yourself"



# Homework / enrichment: worksheet 8.2, questions 2, 5, 6 and the challenge 8.
