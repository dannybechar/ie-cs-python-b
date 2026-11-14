# Warm-up: this code should count how many times a letter appears, but it prints the wrong number. Predict, run, then fix ONE line.
# Tasks 1-5: write your code under each variable and print the answer. Run, compare, then change the value and run again.
# Tip: while you work on one task, put a # before the code of the others, or work in a new file.

text = "sometimes you win sometimes you learn"
letter = "e"
for character in text:
    count = 0
    if character == letter:
        count += 1
print(count)   # should be 5


# Task 1: print True only when text is made of digits only AND has exactly four characters.
# Test values: "2027" -> True, "1.9.2027" -> False, "20x7" -> False, "99" -> False.
# Before you write it, predict and run:
#   text = "I like to play drums"
#   print(text.startswith("I like"))
#   print(text.startswith("play", 10, 17))
#   print(text.startswith("to play", 10, 17))
text = "2027"



# Task 2: count how many times letter appears in text, correctly - walk over the characters with a for loop,
# and do not use count(). Print the answer AFTER the loop.
# Test values: the sentence below with "e" -> 5; "banana" with "a" -> 3; "banana" with "z" -> 0.
text = "sometimes you win sometimes you learn"
letter = "e"



# Task 3: (a) print every letter of text three times, all on one line (end=""), e.g. "Learn" -> LLLeeeaaarrrnnn
# (b) then build the same text as a NEW string with += and print it once, after the loop.
# Test values: "Learn" -> LLLeeeaaarrrnnn, "ab" -> aaabbb.
text = "Learn"



# Task 4: read `number` surnames with input() and print how many contain "cohen" in any letter case.
# Do it twice: version a (with count) and version b (without count - use in).
# Test: number = 3 and the surnames Cohen, Levi, BenCOHEN -> 2.
# Use invented surnames only, never the names of real students.
number = 3



# Task 5: build a new string with only the characters of text that are between "a" and "e"
# (use >= "a" and <= "e") and print it. Predict first: what is printed for "We play on the computer"?
# Other test value: "abcdefg" -> abcde.
text = "We play on the computer"



# If time: print the number of words in text - the number of spaces plus one.
# Test values: "We are learning to program" -> 5. What goes wrong with "two  spaces" (two spaces in a row)?
text = "We are learning to program"
