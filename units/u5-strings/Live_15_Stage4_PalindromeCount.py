# Slide 15 - Stage 4: palindrome and counting
# Run with ROBOT and O; then ANNA; then count a lower-case o.

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

# ---------- new in this step ----------
if name == backwards:
    print("The name reads the same in both directions")
letter = input("Which letter to count? ")
count = 0
for i in range(len(name)):
    if name[i] == letter:
        count += 1
print(letter, "appears", count, "times")
