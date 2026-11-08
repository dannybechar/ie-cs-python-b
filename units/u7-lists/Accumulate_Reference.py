# Unit 7.3 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: removing from a list while a for loop walks over it skips the neighbour of every removed item.
# Trace for [2, 4, 6, 8, 1]: position 0 holds 2 -> removed, the rest slide left;
# position 1 now holds 6 (the 4 was jumped over) -> removed; position 2 holds 1 -> kept. Result [4, 8, 1].
def remove_even_wrong(values):
    for item in values:
        if item % 2 == 0:
            values.remove(item)


# Fixed: build a new list with the numbers to keep (Task 4 does the same without printing)
def remove_even_fixed(values):
    result = []
    for item in values:
        if item % 2 != 0:
            result.append(item)
    return result


def warmup():
    numbers = [2, 4, 6, 8, 1]
    remove_even_wrong(numbers)
    print(numbers)
    print(remove_even_fixed([2, 4, 6, 8, 1]))


# Task 1: accumulation by index and by value
def sum_by_index(values):
    total = 0
    for item in range(len(values)):
        print("item =", item)
        total = total + values[item]
    return total


def sum_by_value(values):
    total = 0
    for item in values:
        print("item =", item)
        total = total + item
    return total


# Task 2: average with an empty-list guard
def calculate_average(values):
    if len(values) == 0:
        return 0
    return sum_by_value_quiet(values) / len(values)


def sum_by_value_quiet(values):
    total = 0
    for item in values:
        total += item
    return total


# Task 3: read prices into a list
def read_prices(count):
    prices = []
    for turn in range(count):
        price = float(input("Enter price: "))
        prices.append(price)
    return prices


def task3():
    prices = read_prices(5)
    print(prices)
    print("total =", sum_by_value_quiet(prices))


# Task 4: a new list instead of changing the old one; a sorted copy
def without_even(values):
    result = []
    for item in values:
        if item % 2 != 0:
            result.append(item)
    return result


def sorted_copy(values):
    copy = values.copy()
    copy.sort()
    return copy


def task4():
    numbers = [5, 2, 8, 1, 4]
    print(without_even(numbers), numbers)
    print(sorted_copy(numbers), numbers)


if __name__ == "__main__":
    warmup()
    # print(sum_by_index([51, 84, 72, 13, 29]))
    # print(sum_by_value([51, 84, 72, 13, 29]))
    # print(calculate_average([25.1, 20.0, 21.5, 24.0, 21.4, 24.5, 21.5, 16.0, 23.3]), calculate_average([]))
    # task3()
    # task4()
