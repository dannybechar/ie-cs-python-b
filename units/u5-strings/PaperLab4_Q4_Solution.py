# Unit 5.4 paper lab - Question 4: a shift cipher (letters move 2 places, the space stays).
text = "hello world"

coded = ""
for ch in text:
    if ch.isalpha():
        coded += chr(ord(ch) + 2)
    else:
        coded += ch
print("Coded:", coded)
