# Unit 5.4 - countdown cases. Write ONE function per case, with the loop the board shows (for or while).
# Replace the word pass with your code. Run the file: each line shows what your function returned
# and what it should return. A line that says None means that function is not written yet.


# Case 1: how many times does "is" appear in the text? Do not use count.
def count_is(text):
    pass


# Case 2: the first letter of every word.
def initials(text):
    pass


# Case 3: every letter becomes the next letter of the alphabet; z becomes a; a space stays.
def next_letters(text):
    pass


# Case 4: the first word and the last word, with one space between them.
def first_and_last_word(text):
    pass


print("Case 1:", count_is("this is his list"), "expected 4")
print("Case 1:", count_is("Mississippi is big"), "expected 3")
print("Case 2:", initials("American Standard Code Information Interchange"), "expected ASCII")
print("Case 2:", initials("grade eight python"), "expected gep")
print("Case 3:", next_letters("abcd"), "expected bcde")
print("Case 3:", next_letters("zoo"), "expected app")
print("Case 3:", next_letters("i like python"), "expected j mjlf qzuipo")
print("Case 4:", first_and_last_word("Cats and dogs are great friends"), "expected Cats friends")
print("Case 4:", first_and_last_word("Hello"), "expected Hello")
