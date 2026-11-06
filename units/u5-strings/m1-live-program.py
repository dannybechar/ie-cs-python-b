# Unit 5.1 live program: Robot ID Card machine - full solution.
# The program is built in five stages; each stage adds lines and the program still runs.

# Stage 1 - read the name and inspect it
name = input("Robot name: ")
print("Type:", type(name))
print("Length:", len(name))

# Stage 2 - single letters: first, last, and any position the user asks for
first = name[0]
last = name[-1]
print("First letter:", first)
print("Last letter:", last)
pos = int(input("Which position? "))
if pos < len(name) and pos >= -len(name):
    print("The letter at position", pos, "is", name[pos])
else:
    print("There is no position", pos, "in", name)

# Stage 3 - build the code from new strings (a string cannot be changed in place)
code = first + last + "-" + str(len(name))
print("Code:", code)

# Stage 4 - the framed card
border = "*" * (len(name) + 4)
print(border)
print("* " + name + " *")
print(border)

# Stage 5 - the age: input is text, so convert it to a number
age = int(input("Robot age: "))
print("Next year the robot will be", age + 1)
print("Written twice as text:", str(age) * 2)
