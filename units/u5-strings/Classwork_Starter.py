# Unit 5.3 classwork. Paper first: predict or write on the worksheet, THEN run here to check.
# Part A: do NOT run before you wrote your prediction on paper. Part B: write each function on paper first.


# ---------------- Part A: read, predict, run -----------------------------------------------------

def a1():
    for ch in "sometimes":
        print(ch, end=",")
    print()


def a2():
    new_text = ""
    for ch in "We play on the computer":
        if ch >= "a" and ch <= "e":
            new_text = new_text + ch
    print(new_text)


def a3():
    sentence = "We are learning to program"
    count = 0
    for ch in sentence:
        if ch == " ":
            count += 1
    print(sentence)
    print("Number of words:", count + 1)


def a4():
    count = 0
    for ch in "banana":
        if ch == "a":
            count += 1
    return count


# ---------------- B1: find the bug (it should return 5) -------------------------------------------

def count_letter(text, letter):
    for ch in text:
        count = 0
        if ch == letter:
            count += 1
    return count


# ---------------- B2 - B5: write the function (replace the word pass) ---------------------------

def count_char(text, letter):
    pass


def triple(text):
    pass


def count_letters(text):
    pass


def count_digits(text):
    pass


def count_vowels(text):
    pass


# ---------------- Homework: write on paper first ------------------------------------------------

def only_digits(text):
    pass


def hide_digits(text):
    pass


# ---------------- Checks: compare with the "expected" column on the worksheet --------------------

sentence = "sometimes you win sometimes you learn"
print("B1:", count_letter(sentence, "e"))
print("B2:", count_char(sentence, "e"), count_char("banana", "a"), count_char("banana", "x"), count_char("", "a"))
print("B3:", triple("Learn"))
ai = "In 2024 the model answered 3 questions."
print("B4:", count_letters(ai), count_digits(ai))
print("B5:", count_vowels("Hello World"), count_vowels("rhythm"), count_vowels("AEIOU"))
print("B6:", only_digits("In 2027 I turn 15"))
print("B7:", hide_digits("Room 12 floor 3"))
