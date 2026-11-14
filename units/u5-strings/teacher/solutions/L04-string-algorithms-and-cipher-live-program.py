# Lessons 8.2–8.7 live program: Secret Message Machine - full solution.
# The program is built in six stages; each stage adds lines and the program still runs.
# Use only invented messages.

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

# Stage 2 - letters are numbers: ord and chr
first = message[0]
last = message[-1]
print("First:", first, ord(first))
print("Last:", last, ord(last))
print("Next after first:", chr(ord(first) + 1))

# Stage 3 - the shift cipher: move every letter forward, wrap after z (or Z), keep other characters
coded = ""
for ch in message:
    if ch.isalpha():
        code = ord(ch) + shift
        if ch == ch.lower():
            end = ord("z")
        else:
            end = ord("Z")
        if code > end:
            code -= 26
        coded += chr(code)
    else:
        coded += ch
print("Coded:", coded)

# Stage 4 - two more new strings: the number cipher and the initials
numbers = ""
for ch in message:
    numbers += str(ord(ch)) + " "
initials = message[0]
for index in range(1, size):
    if message[index - 1] == " ":
        initials += message[index]
print("Numbers:", numbers)
print("Initials:", initials)

# Stage 5 - the report: a frame around the coded message, and split / join shown only
line = "*" * (len(coded) + 4)
print(line)
print("*", coded, "*")
print(line)
print("Dashes:", "-".join(coded.split(" ")))

# Stage 6 - the receiver: ask for the code word (the initials), then decode and compare
code_word = input("Code word: ")
while code_word.lower() != initials.lower():
    print("Wrong code word")
    code_word = input("Code word: ")
decoded = ""
for ch in coded:
    if ch.isalpha():
        code = ord(ch) - shift
        if ch == ch.lower():
            start = ord("a")
        else:
            start = ord("A")
        if code < start:
            code += 26
        decoded += chr(code)
    else:
        decoded += ch
print("Decoded:", decoded)
if decoded == message:
    print("Match: yes")
else:
    print("Match: no")
