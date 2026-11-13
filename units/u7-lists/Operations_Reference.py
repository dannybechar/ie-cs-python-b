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


# Task 2 (Ministry 12.1 p. 24): a name that is in the list is counted, a new name is added
def name_check(names, name):
    if name in names:
        print(name, "appears", names.count(name), "times")
    else:
        names.append(name)
        print(name, "was added")


def task2():
    names = ["Dana", "Avi", "Dana", "Noa"]
    name_check(names, "Dana")
    name_check(names, "dana")
    name_check(names, "Lior")
    print(names)


# Task 3: palindromes, using the slice [::-1] and lower()
def all_palindromes(words):
    for word in words:
        word = word.lower()
        if word != word[::-1]:
            return False
    return True


# Task 4 (Ministry 9.1 pp. 38-40, the "Sandwich" challenge): split and join, no + operator.
# Words whose first letter equals their last letter.
def sandwich(text):
    result = []
    for word in text.split():
        if word[0] == word[-1]:
            result.append(word)
    return " ".join(result)


# Task 5 (Ministry 9.3, the "even list"): even length, and the first half equals the second half
def even_list(values):
    half = len(values) // 2
    return len(values) % 2 == 0 and values[:half] == values[half:]


# If time (a): Ministry 12.0 p. 23 - first and last names sit in pairs (even cell = first name,
# odd cell = last name); count the pairs that start with the same letter, ignoring case
def same_initials(names):
    count = 0
    for index in range(0, len(names), 2):
        if names[index][0].lower() == names[index + 1][0].lower():
            count += 1
    return count


# If time (b): split, join, random.choice (Ministry 12.1 pp. 12-15 and 34-36)
def to_sentence(text):
    words = text.split("#")
    return " ".join(words)


def random_word(text):
    words = text.split("#")
    return random.choice(words)


def great_match(names):
    num = ord(random.choice(names)) + ord(random.choice(names))
    return num % 7 == 0


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
    animals = ["Giraffe", "Lion", "Hippo", "Giraffe", "Duck", "Giraffe", "Cat", "Giraffe"]
    print(animals.count("Giraffe"), animals.count("Dog"), animals.count("cat"))
    print("giraffe" in animals, "Giraffe" in animals)
    print(animals.index("Giraffe"))
    animals.remove("Giraffe")
    print(animals)
    last = animals.pop()
    print(last, animals)
    first = animals.pop(0)
    print(first, animals)
    numbers = [30, 10, 20]
    result = numbers.sort()
    print(result, numbers)
    numbers.sort(reverse=True)
    print(numbers)
    numbers = [1, 5, 2, 9, 3]
    numbers.reverse()
    print(numbers)
    print(list("I love python"))
    print("a-b-c".split("-"))
    print("a b  c".split())
    print("@".join(["guitar", "piano", "drums"]))
    colors = ["red", "blue", "green", "yellow"]
    for item in range(6):
        print(colors[item % 4], end="\t")
        print(item)


# The 13-row summary table (Ministry 9.1 pp. 42-43 and the help sheet): what is returned, and the list after
def table_demo():
    lst = [1, 2, 3]
    print("len", len(lst), lst)
    lst = [1, 2, 2, 3]
    print("count", lst.count(2), lst)
    lst = [1, 2, 3]
    print("in", 2 in lst, lst)
    print("index", lst.index(2), lst)
    lst = [1, 2, 3, 2]
    print("remove", lst.remove(2), lst)
    lst = [1, 2, 3]
    print("pop", lst.pop(0), lst)
    lst = [1, 2]
    print("append", lst.append(3), lst)
    lst = [1, 3]
    print("insert", lst.insert(1, 2), lst)
    lst = [3, 1, 2]
    print("sort", lst.sort(), lst)
    lst = [1, 2, 3]
    print("reverse", lst.reverse(), lst)
    print("list", list("abc"))
    lst = ["a", "b", "c"]
    print("join", "?".join(lst), lst)
    print("split", "a?b?c".split("?"))


if __name__ == "__main__":
    warmup()
    # demo()
    # table_demo()
    # print(colder_than([25, 20, 21, 24, 21, 24, 21, 16, 23], 21))
    # task2()
    # print(all_palindromes(["ABA", "1221", "A12321A"]))
    # print(sandwich("anna told bob he won level two!"))
    # print(even_list(["A", "b", "c", "A", "b", "c"]))
    # print(same_initials(["Amit", "Berkovich", "chen", "Cohen", "Daniel", "levi", "dana", "dikla", "Carmi", "Cohen"]))
    # print(to_sentence("One#Apple#a#day#keeps#the#doctor#away"))
    # print(random_word("One#Apple#a#day#keeps#the#doctor#away"))
