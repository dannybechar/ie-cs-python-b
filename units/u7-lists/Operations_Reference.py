# Unit 7.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.
import random


# Warm-up, fixed: the loop variable is item, so append(item) - there is no variable called i
def warmup():
    temperature = [25, 20, 21, 24, 21, 24, 21, 16, 23]
    new_list = []
    for item in temperature:
        if item < 21:
            new_list.append(item)
    print(new_list)


# Task 1: build a NEW list inside a function
def colder_than(values, limit):
    result = []
    for item in values:
        if item < limit:
            result.append(item)
    return result


# Task 2: in + append - no duplicate names
def join_class(students, name):
    if name in students:
        print("We cannot place you in this class")
        return False
    students.append(name)
    return True


def task2():
    students = ["Dana", "Avi", "Noa"]
    print(join_class(students, "Avi"), students)
    print(join_class(students, "Lior"), students)


# Task 3: palindromes, using the slice [::-1] and lower()
def all_palindromes(words):
    for word in words:
        word = word.lower()
        if word != word[::-1]:
            return False
    return True


# Task 4: split and join, random.choice
def to_sentence(text):
    words = text.split("#")
    return " ".join(words)


def random_word(text):
    words = text.split("#")
    return random.choice(words)


# Teacher demo for the first 45 minutes (every line of it is shown in the notes)
def demo():
    my_lst = list()
    my_lst.append(1)
    my_lst.append(2)
    my_lst.append(3)
    print(my_lst)
    my_lst.insert(0, 4)
    print(my_lst)
    my_lst.extend([7, 8])
    print(my_lst)
    my_lst.append([7, 8])
    print(my_lst)
    letters = ["c", "a", "d", "a"]
    print(letters.count("a"), letters.index("a"))
    letters.remove("a")
    print(letters)
    last = letters.pop()
    print(last, letters)
    first = letters.pop(0)
    print(first, letters)
    numbers = [30, 10, 20]
    result = numbers.sort()
    print(result, numbers)
    numbers.reverse()
    print(numbers)
    print(list("cat"))
    print("-".join(["a", "b", "c"]))
    print("a-b-c".split("-"))


if __name__ == "__main__":
    warmup()
    # print(colder_than([25, 20, 21, 24, 21, 24, 21, 16, 23], 21))
    # task2()
    # print(all_palindromes(["ABA", "1221", "A12321A"]))
    # print(to_sentence("One#Apple#a#day#keeps#the#doctor#away"))
    # print(random_word("One#Apple#a#day#keeps#the#doctor#away"))
