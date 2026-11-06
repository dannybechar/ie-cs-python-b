# Unit 5.2 paper lab - Question 2: an item code (full solution, plain code, no functions).

# a. a code with exactly 2 dashes; ask again until it is valid
code = input("Code: ")
while code.count("-") != 2:
    print("Need exactly 2 dashes")
    code = input("Code: ")

# b. cut into three parts; the second dash is searched after the first one
first = code.find("-")
second = code.find("-", first + 1)
part1 = code[:first]
part2 = code[first + 1:second]
part3 = code[second + 1:]
print("Part 1:", part1)
print("Part 2:", part2)
print("Part 3:", part3)

# c. the parts in reverse order, and the code without the dashes
print(part3 + "/" + part2 + "/" + part1)
print(code.replace("-", ""))

# d. a hidden version, and the whole code backwards
print(part1 + "-" + "*" * len(part2) + "-" + part3)
print("Mirror:", code[::-1])
