# Unit 5.4 - reference for the teacher.
# One task per function; run ONE at a time by removing the # from its call at the bottom.


# Warm-up, explained: `character == "a" or "e" or ...` reads as (character == "a") or "e" or ...
# and a non-empty string such as "e" is always True. Fix: character in "aeiou"
def count_vowels(text):
    total = 0
    for character in text:
        if character in "aeiou":
            total += 1
    return total


def warmup():
    print(count_vowels("sometimes you learn"))


# Task 1: Ministry exercise 4 - first word and last word, no lists
def first_and_last_word(text):
    first_space = text.find(" ")
    if first_space == -1:
        return text
    last_space = first_space
    for index in range(len(text)):
        if text[index] == " ":
            last_space = index
    return text[:first_space] + " " + text[last_space + 1:]


def task1():
    print(first_and_last_word("Cats and dogs are great friends"))
    print(first_and_last_word("Hello"))


# Task 2: Ministry exercise 5 - a word starts right after a space
def initials(text):
    if text == "":
        return ""
    result = text[0]
    for index in range(1, len(text)):
        if text[index - 1] == " ":
            result += text[index]
    return result


def task2():
    print(initials("American Standard Code Information Interchange"))


# Task 3: Ministry exercise 6 - "is" also hides inside "this" and "his"
def count_is_a(text):
    return text.count("is")


def count_is_b(text):
    total = 0
    for index in range(len(text) - 1):
        if text[index:index + 2] == "is":
            total += 1
    return total


def task3():
    print(count_is_a("this is his list"))
    print(count_is_b("this is his list"))


# Task 4: Ministry exercise 7 - one pass, five counters
def print_vowels(text):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for character in text:
        if character == "a":
            a += 1
        elif character == "e":
            e += 1
        elif character == "i":
            i += 1
        elif character == "o":
            o += 1
        elif character == "u":
            u += 1
    print("a:", a)
    print("e:", e)
    print("i:", i)
    print("o:", o)
    print("u:", u)


def print_vowels_with_count(text):
    for vowel in "aeiou":
        print(vowel + ":", text.count(vowel))


def task4():
    print_vowels("sometimes you learn")
    print_vowels_with_count("sometimes you learn")


# Task 5: ord and chr - the next-letter cipher (the Ministry's solution printed "a" on a line of its own;
# building a string and returning it fixes that)
def next_letters(text):
    result = ""
    for character in text:
        if character == "z":
            result += "a"
        elif character >= "a" and character < "z":
            result += chr(ord(character) + 1)
        else:
            result += character
    return result


def task5():
    for character in "Hello":
        print(ord(character), end=",")
    print()
    print(next_letters("abcd"))
    print(next_letters("zoo"))
    print(next_letters("i like python"))


# Task 6: split and join - the list is only shown and printed here (lists are Unit 7)
def dash_words(text):
    return "-".join(text.split(" "))


def task6():
    text = "guitar piano drums"
    print(text.split(" "))
    print(dash_words(text))
    print(text.replace(" ", "-"))


# Checkpoint 1: worksheet 8.2 question 3
def middle(word):
    half = len(word) // 2
    if len(word) % 2 == 1:
        return word[half]
    return word[half - 1:half + 1]


# Checkpoint 2: worksheet 8.2 question 4 (returns the text instead of printing it)
def edges(text):
    if len(text) < 4:
        return "****"
    return text[:4] + text[-4:]


# Checkpoint 3: worksheet 8.2 question 7. Alternate by LETTER, not by index: the space must not count,
# so the index-parity hint in the worksheet would give "TrUsT YoUrSeLf".
def alternate_case(text):
    result = ""
    upper_next = True
    for character in text:
        if character == " ":
            result += " "
        elif upper_next:
            result += character.upper()
            upper_next = False
        else:
            result += character.lower()
            upper_next = True
    return result


def checkpoint():
    print(middle("robot"))
    print(middle("python"))
    print(edges("I like to play drums"))
    print(edges("abc"))
    print(alternate_case("trust yourself"))


# Enrichment - worksheet 8.2 questions 2, 5, 6, 8 (challenge)
def star_between(text):
    return text[0] + "*" + text[-1]


def last_letters(text):
    result = ""
    for index in range(len(text)):
        if index == len(text) - 1 or text[index + 1] == " ":
            result += text[index]
    return result


# the WORD "it" - counting the characters "it" would also find the "it" inside "with" and "little"
def count_word_it(text):
    total = 0
    word = ""
    for character in text + " ":
        if character == " ":
            if word == "it":
                total += 1
            word = ""
        else:
            word += character
    return total


# challenge: the second word and the word before the last (needs at least three words)
def second_and_before_last(text):
    first_space = text.find(" ")
    second_space = text.find(" ", first_space + 1)
    second_word = text[first_space + 1:second_space]
    last_space = -1
    before_last_space = -1
    for index in range(len(text)):
        if text[index] == " ":
            before_last_space = last_space
            last_space = index
    return second_word + " " + text[before_last_space + 1:last_space]


def enrichment():
    sentence = "Cats and dogs are great friends"
    print(star_between(sentence))
    print(last_letters("American Standard Code Information Interchange"))
    print(count_word_it("it is a little bit with it"))
    print(second_and_before_last(sentence))


warmup()
# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# checkpoint()
# enrichment()
