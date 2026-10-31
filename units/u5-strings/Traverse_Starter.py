# Warm-up: count_letter should count how many times a letter appears, but it prints the wrong number. Predict, run, then fix ONE line.

def count_letter(text, letter):
    for character in text:
        count = 0
        if character == letter:
            count += 1
    return count


print(count_letter("sometimes you win sometimes you learn", "e"))   # should be 5


# Task 1: write is_year(text) - return True only when text is made of digits only AND has exactly four characters.
# Test: "2027" True, "1.9.2027" False, "20x7" False, "99" False.
# Before you write it, predict and run:
#   text = "I like to play drums"
#   print(text.startswith("I like"))
#   print(text.startswith("play", 10, 17))
#   print(text.startswith("to play", 10, 17))


# Task 2: write count_letter again, correctly, as a NEW function called count_char(text, letter) - walk over the
# characters with a for loop, and do not use count(). Test: the sentence above with "e" gives 5.


# Task 3: write triple_print(text) - print every letter three times, all on one line (end=""), e.g. "Learn" -> LLLeeeaaarrrnnn
# Then write triple(text) - the same, but build a NEW string with += and RETURN it instead of printing.


# Task 4: write count_cohen(number) - read `number` surnames with input() and return how many contain "cohen"
# in any letter case. Do it twice: count_cohen_a (with count) and count_cohen_b (without count - use in).
# Use invented surnames only, never the names of real students.


# Task 5: write keep_a_to_e(text) - build and return a new string with only the characters that are between "a" and "e"
# (use >= "a" and <= "e"). Predict first: what does it return for "We play on the computer"?


# If time: write count_words(text) - the number of spaces plus one. What goes wrong when a text has two spaces in a row?
