# Unit 5.1 paper lab - reference solutions, one block per question (plain code, no functions).
# Each block is separate: run one block at a time (comment out the others) with the inputs in its comment.

# === Question 1 ===
word = "STAR"
result = ""
for i in range(len(word)):
    result = word[i] + result
    print(i, result)
print(result)

# === Question 2 (fixed) ===
word = "STAR"
for i in range(len(word)):
    print(i, word[i])

# === Question 3 === inputs: ox, FALCON
callsign = input("Callsign: ")
while len(callsign) < 4:
    print("Too short, try again")
    callsign = input("Callsign: ")
first = callsign[0]
last = callsign[-1]
print("First:", first)
print("Last:", last)
print("Length:", len(callsign))
print("Code: " + first + last + "-" + str(len(callsign)))

# === Question 4 === inputs: BANANA, A
message = input("Message: ")
letter = input("Letter: ")
stars = ""
count = 0
for i in range(len(message)):
    if i > 0:
        stars = stars + "*"
    stars = stars + message[i]
    if message[i] == letter:
        count += 1
print(stars)
print(letter, "appears", count, "times")

# --- if time: reads the same in both directions ---
backwards = ""
for i in range(len(message)):
    backwards = message[i] + backwards
if message == backwards:
    print("Same both ways")

# === Question 5 === inputs: LUNA, 200, 12
name = input("Name: ")
age = int(input("Age: "))
while age < 1 or age > 120:
    print("Age must be 1 to 120")
    age = int(input("Age: "))
border = "*" * (len(name) + 4)
print(border)
print("* " + name + " *")
print(border)
print("Seat: " + name[0] + str(age))
print("Next year:", age + 1)

# === Exit check === text = "PLANET": P, E, 6, IndexError (the last index is len(text) - 1: T)
text = "PLANET"
print(text[0])
print(text[-2])
print(len(text))
# print(text[len(text)])
