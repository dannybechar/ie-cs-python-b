# Unit 5.3 - reference for the teacher.
# One task per function; run ONE at a time by removing the # from its call at the bottom.


# Warm-up, explained: count = 0 sits INSIDE the loop, so the counter restarts from zero for every character.
# It must be set once, before the loop.
def count_letter(text, letter):
    count = 0
    for character in text:
        if character == letter:
            count += 1
    return count


def warmup():
    print(count_letter("sometimes you win sometimes you learn", "e"))


# Task 1: isdigit + len (worksheet 7.2, questions 12 and 14 first, as a predict-and-check)
def is_year(text):
    return text.isdigit() and len(text) == 4


def task1():
    text = "I like to play drums"
    print(text.startswith("I like"))
    print(text.startswith("play", 10, 17))
    print(text.startswith("to play", 10, 17))
    print(is_year("2027"))
    print(is_year("1.9.2027"))
    print(is_year("20x7"))
    print(is_year("99"))


# Task 2: count with a for loop, no count() (Ministry exercise 1)
def count_char(text, letter):
    count = 0
    for character in text:
        if character == letter:
            count += 1
    return count


def task2():
    print(count_char("sometimes you win sometimes you learn", "e"))


# Task 3: print with end="" (Ministry exercise 2), then build the same string and return it
def triple_print(text):
    for character in text:
        print(character * 3, end="")
    print()


def triple(text):
    result = ""
    for character in text:
        result += character * 3
    return result


def task3():
    triple_print("Learn")
    print(triple("Learn"))


# Task 4: Ministry exercise 3 - reads the surnames itself (run with typed or piped input)
def count_cohen_a(number):
    total = 0
    for turn in range(number):
        surname = input("Surname: ").lower()
        if surname.count("cohen") > 0:
            total += 1
    return total


def count_cohen_b(number):
    total = 0
    for turn in range(number):
        surname = input("Surname: ").lower()
        if "cohen" in surname:
            total += 1
    return total


def task4():
    print(count_cohen_b(3))


# Task 5: build a new string from selected characters (the code on the Ministry slide)
def keep_a_to_e(text):
    result = ""
    for character in text:
        if character >= "a" and character <= "e":
            result += character
    return result


def task5():
    print(keep_a_to_e("We play on the computer"))


# If time: spaces + 1 = words, as long as every gap is a single space
def count_words(text):
    spaces = 0
    for character in text:
        if character == " ":
            spaces += 1
    return spaces + 1


def task6():
    print(count_words("We are learning to program"))
    print(count_words("two  spaces"))     # 3, not 2 - a gap of two spaces counts twice


warmup()
# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
