# Step 2 (slide 11): letters are numbers - ord and chr
# Run with Meet at old bridge and shift 3.

# Stage 1 - read a message (at least 5 characters) and a shift (1 to 25); facts about the message
message = input("Message: ")
while len(message) < 5:
    print("Too short, try again")
    message = input("Message: ")
shift = int(input("Shift (1-25): "))
while shift < 1 or shift > 25:
    print("Shift must be 1 to 25")
    shift = int(input("Shift (1-25): "))
size = len(message)
words = message.count(" ") + 1
if size % 2 == 1:
    middle = message[size // 2]
else:
    middle = message[size // 2 - 1:size // 2 + 1]
print("Length:", size)
print("Words:", words)
print("Middle:", middle)

# ---------- new in this step ----------
# Stage 2 - letters are numbers: ord and chr
first = message[0]
last = message[-1]
print("First:", first, ord(first))
print("Last:", last, ord(last))
print("Next after first:", chr(ord(first) + 1))
