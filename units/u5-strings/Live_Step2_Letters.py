# Step 2 (slides 7-10): first, last and a chosen position
# Run with ROBOT and positions 2, -2 and 9.

# Stage 1 - read the name; ask again until it has at least 3 characters
name = input("Robot name: ")
while len(name) < 3:
    print("Name too short, try again")
    name = input("Robot name: ")
print("Length:", len(name))

# ---------- new in this step ----------
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
