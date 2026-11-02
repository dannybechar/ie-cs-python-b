# Unit 5.4 - worksheet. Question 1: find the bug in count_vowels (predict first, then run).
# Questions 2-5: replace the word pass with your function. Run the file and compare with "expected".


# Question 1: this function should count the vowels. Predict what it prints, run, explain, fix.
def count_vowels(text):
    total = 0
    for character in text:
        if character == "a" or "e" or "i" or "o" or "u":
            total += 1
    return total


# Question 2: the middle letter; two letters when the length is even.
def middle(word):
    pass


# Question 3: the first 4 and the last 4 characters; "****" when the text is shorter than 4.
def edges(text):
    pass


# Question 4: the last letter of every word.
def last_letters(text):
    pass


# Question 5: letters alternate UPPER / lower; a space stays and does not count.
def alternate_case(text):
    pass


# If time: how many times does the WORD "it" appear?
def count_word_it(text):
    pass


print("Q1:", count_vowels("sometimes you learn"), "expected 8")
print("Q2:", middle("robot"), middle("python"), middle("a"), "expected b th a")
print("Q3:", edges("I like to play drums"), edges("abc"), edges("abcd"), "expected I lirums **** abcdabcd")
print("Q4:", last_letters("I like to play drums"), last_letters("Hello"), "expected Ieoys o")
print("Q5:", alternate_case("trust yourself"), alternate_case("ai"), "expected TrUsT yOuRsElF Ai")
print("If time:", count_word_it("it is a little bit with it"), "expected 2")
