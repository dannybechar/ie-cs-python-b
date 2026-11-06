# Slide 7 - Stage 2: first and last letter
# Run with ROBOT.

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
