# Unit 5.1 paper lab - reference solutions, one block per question (plain code, no functions).
# Each block is separate: run one block at a time (comment out the others) with the inputs shown in its title.

# === Question 1 === expected: RATS
word = "STAR"
result = ""
for i in range(len(word)):
    result = word[i] + result
print(result)

# === Question 2 === expected: 3
word = "BANANA"
letter = "A"
count = 0
for i in range(len(word)):
    if word[i] == letter:
        count += 1
print(count)

# === Question 3 === expected: S-T-A-R
word = "STAR"
result = ""
for i in range(len(word)):
    if i > 0:
        result = result + "-"
    result = result + word[i]
print(result)

# === Question 4 === expected: FN-6
word = "FALCON"
print(word[0] + word[-1] + "-" + str(len(word)))

# === Question 5 === inputs: abc, planet
password = input("Password: ")
while len(password) < 6:
    print("Too short")
    password = input("Password: ")
print("Welcome")

# === Question 6 === input: LUNA
name = input("Name: ")
border = "*" * (len(name) + 4)
print(border)
print("* " + name + " *")
print(border)
