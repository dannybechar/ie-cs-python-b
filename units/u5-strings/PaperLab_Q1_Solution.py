# Unit 5.1 paper lab - Question 1: a word and its letters (full solution, plain code, no functions).
word = "BANANA"

# a. length, first letter, last letter
print("Length:", len(word))
print("First:", word[0])
print("Last:", word[-1])

# b. every character with its place from the start and from the end
for i in range(len(word)):
    print(i, i - len(word), word[i])

# c. the word in reverse, and a message if it reads the same both ways
reversed_word = ""
for i in range(len(word)):
    reversed_word = word[i] + reversed_word
print("Reversed:", reversed_word)
if word == reversed_word:
    print("The word reads the same both ways")

# d. count a letter chosen by the user
letter = input("Letter: ")
count = 0
for i in range(len(word)):
    if word[i] == letter:
        count += 1
if count > 0:
    print(letter, "appears", count, "times")
else:
    print(letter, "does not appear")
