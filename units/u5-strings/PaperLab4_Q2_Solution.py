# Unit 5.4 paper lab - Question 2: a secret word (full solution, plain code, no functions).
word = "bike"

# a. letters are numbers: the number of the first letter and the next letter
print("Number of first letter:", ord(word[0]))
print("Next letter:", chr(ord(word[0]) + 1))

# b. shift every letter 3 places forward
secret = ""
for ch in word:
    secret += chr(ord(ch) + 3)
print("Secret word:", secret)

# c. number code: the place of every letter in the alphabet, with dashes between
numbers = ""
for ch in word:
    if numbers != "":
        numbers += "-"
    numbers += str(ord(ch) - 96)
print("Number code:", numbers)

# d. decode: shift the secret word 3 places back and compare with the original
decoded = ""
for ch in secret:
    decoded += chr(ord(ch) - 3)
print("Decoded:", decoded)
if decoded == word:
    print("The code works")
else:
    print("The code is broken")
