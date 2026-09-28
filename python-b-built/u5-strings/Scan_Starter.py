# Warm-up: this should print every character of "AI 2026". Run it, read the error, then fix the range.

text = "AI 2026"
for index in range(len(text) + 1):
    print(index, text[index])


# Task 1: write count_maybe(text) - returns how many times "maybe" appears, ignoring case.
# Test on "Maybe it works. MAYBE verify it."


# Task 2: write first_part(text) - returns everything before the first space.
# If there is no space, return the whole text. Test on "smart assistant" and on "Python".


# Task 3: write hide_digits(text) - returns the text with every digit replaced by "#".
# Do not use .replace() once per digit. Test on "Room 12 at 09:30".
