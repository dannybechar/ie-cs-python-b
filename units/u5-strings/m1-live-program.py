# Unit 5.1 live program: Robot ID Card machine - full solution.
# The program is built in six stages; each stage adds lines and the program still runs.

# Stage 1 - read the name; ask again until it has at least 3 characters
name = input("Robot name: ")
while len(name) < 3:
    print("Name too short, try again")
    name = input("Robot name: ")
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

# Stage 3 - walk through the name with a loop: place, negative place, letter
for i in range(len(name)):
    print(i, i - len(name), name[i])

# Stage 4 - build new strings in a loop: dashed, reversed, and count one letter
dashed = ""
backwards = ""
for i in range(len(name)):
    if i > 0:
        dashed = dashed + "-"
    dashed = dashed + name[i]
    backwards = name[i] + backwards
print("Dashed:", dashed)
print("Backwards:", backwards)
if name == backwards:
    print("The name reads the same in both directions")
letter = input("Which letter to count? ")
count = 0
for i in range(len(name)):
    if name[i] == letter:
        count += 1
print(letter, "appears", count, "times")

# Stage 5 - the code and the framed card (the frame fits the longest line)
code = first + last + "-" + str(len(name))
print("Code:", code)
line1 = dashed
line2 = "Code: " + code
width = len(line1)
if len(line2) > width:
    width = len(line2)
border = "*" * (width + 4)
print(border)
gap1 = " " * (width - len(line1))
gap2 = " " * (width - len(line2))
print("* " + line1 + gap1 + " *")
print("* " + line2 + gap2 + " *")
print(border)

# Stage 6 - the age: ask until it is between 1 and 120; input is text, so convert it
age = int(input("Robot age: "))
while age < 1 or age > 120:
    print("Age must be between 1 and 120")
    age = int(input("Robot age: "))
print("Next year the robot will be", age + 1)
print("Written twice as text:", str(age) * 2)
