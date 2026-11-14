# Step 1 (slides 9-10): the message, the shift and facts about the message
# Run: type hi (too short), then Meet at old bridge; shift 30 (bad), then 3.

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
