# Slide 10 - Without the if: IndexError
# Run with ROBOT and position 9 - the program stops with an error.

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

# ---------- new in this step ----------
pos = int(input("Which position? "))
print("The letter at position", pos, "is", name[pos])
