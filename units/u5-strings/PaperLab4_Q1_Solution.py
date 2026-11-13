# Unit 5.4 paper lab - Question 1: a song title (full solution, plain code, no functions).
title = "moon light sonata"

# a. first, last and middle character
print("First:", title[0])
print("Last:", title[-1])
print("Length:", len(title))
print("Middle:", title[len(title) // 2])

# b. how many words: the number of spaces plus one
spaces = title.count(" ")
words = spaces + 1
print("Words:", words)

# c. the initials: the first letter, and every letter that comes after a space
initials = title[0].upper()
for i in range(1, len(title)):
    if title[i - 1] == " ":
        initials += title[i].upper()
print("Initials:", initials)

# d. a new title with a capital letter at the start of every word
fixed = ""
for i in range(len(title)):
    if i == 0 or title[i - 1] == " ":
        fixed += title[i].upper()
    else:
        fixed += title[i]
print("Fixed title:", fixed)
print("Short name:", initials + str(words))
