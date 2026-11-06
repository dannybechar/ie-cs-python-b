# Unit 5.1 paper lab - reference solutions (plain code, no functions).
# Question 1 and Question 2 are separate programs: run one at a time (comment out the other).

# ===================== Question 1 =====================
word = "BANANA"

# a.
print("Length:", len(word))
print("First:", word[0])
print("Last:", word[-1])

# b.
for i in range(len(word)):
    print(i, i - len(word), word[i])

# c.
reversed_word = ""
for i in range(len(word)):
    reversed_word = word[i] + reversed_word
print("Reversed:", reversed_word)
if word == reversed_word:
    print("The word reads the same both ways")

# d. (inputs: A, then try Z)
letter = input("Letter: ")
count = 0
for i in range(len(word)):
    if word[i] == letter:
        count += 1
if count > 0:
    print(letter, "appears", count, "times")
else:
    print(letter, "does not appear")


# ===================== Question 2 =====================
# a. (inputs: ab, falcon)
username = input("Username: ")
while len(username) < 4 or len(username) > 10:
    print("Must be 4 to 10 characters")
    username = input("Username: ")

# b.
print("Masked: " + username[0] + "*" * (len(username) - 1))

# c. (inputs: 200, 12)
age = int(input("Age: "))
while age < 1 or age > 120:
    print("Age must be 1 to 120")
    age = int(input("Age: "))
print("Next year you will be", age + 1)

# d.
line1 = username
line2 = "Age: " + str(age)
width = len(line1)
if len(line2) > width:
    width = len(line2)
border = "*" * (width + 4)
gap1 = " " * (width - len(line1))
gap2 = " " * (width - len(line2))
print(border)
print("* " + line1 + gap1 + " *")
print("* " + line2 + gap2 + " *")
print(border)
