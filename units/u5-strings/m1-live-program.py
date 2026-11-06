# Unit 5.1 live program: Robot ID Card (teacher types it step by step with the class).
# Problem: the user types a robot's name and age. Print a framed card with the name,
# its length, a two-letter code (first + last letter) and the age next year.
# Lines marked "# ERROR DEMO" are typed live to show the error, then deleted or fixed.


# STEP 0 - an AI answer is a string (type, then delete these lines)
answer = "Take a short break and drink water."
print(type(answer))
print(len(answer))
print(answer[0])


# STEP 1 - input gives a string
name = input("Robot name: ")
print(type(name))
empty = ""
print(len(empty))


# STEP 2 - length
print("Length:", len(name))


# STEP 3 - positive and negative indexes
first = name[0]
last = name[-1]
print(first, last)
print(name[2])
print(name[-2])


# STEP 4 - one index too far
# ERROR DEMO: IndexError: string index out of range
# print(name[len(name)])
print(name[len(name) - 1])


# STEP 5 - + joins, * repeats: the framed card
border = "*" * (len(name) + 4)
print(border)
print("* " + name + " *")
print(border)


# STEP 6 - the code, and str() for numbers inside text
code = first + last
print("Code:", code)
# ERROR DEMO: TypeError: can only concatenate str (not "int") to str
# print("Length: " + len(name))
print("Length: " + str(len(name)))


# STEP 7 - age: input is text, int() makes it a number
# ERROR DEMO (shows 77 for "7"): age = input("Age: ") then print(age + age)
age = int(input("Age: "))
print("Next year:", age + 1)


# STEP 8 - strings cannot be changed in place
# ERROR DEMO: TypeError: 'str' object does not support item assignment
# name[0] = "r"


# STEP 9 - the same idea on other words (plain code, no functions yet)
word = "A"
print(word[0] + word[-1])
word = "hello"
print("*" * len(word))


# STEP 10 - exit check
text = "MODEL"
print(text[1])
print(text[-1])
print(len(text))
# ERROR DEMO: IndexError: string index out of range
# print(text[len(text)])
