# Step 3 (slide 11): walk through the name with a loop
# Run with ROBOT; then try a longer name.

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

# ---------- new in this step ----------
# Stage 3 - walk through the name with a loop: place, negative place, letter
for i in range(len(name)):
    print(i, i - len(name), name[i])
