# Lessons 8.0–8.1 paper lab - Question 1: analysing a message (full solution, plain code, no functions).
message = "Was it a car or a cat I saw?"

# a. upper and lower case copies, and two yes/no questions
print(message.upper())
print(message.lower())
print("Starts with was:", message.lower().startswith("was"))
print("Ends with a question mark:", message.endswith("?"))

# b. one loop over the characters: count letters, digits and everything else
letters = 0
digits = 0
others = 0
for ch in message:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        others += 1
print("Letters:", letters)
print("Digits:", digits)
print("Others:", others)

# c. a new string with the letters only, in lower case
only_letters = ""
for ch in message:
    if ch.isalpha():
        only_letters += ch.lower()
print("Letters only:", only_letters)

# d. build the letters-only string backwards and compare
backwards = ""
for ch in only_letters:
    backwards = ch + backwards
print("Backwards:", backwards)
if only_letters == backwards:
    print("The message reads the same both ways")
else:
    print("The message does not read the same both ways")
