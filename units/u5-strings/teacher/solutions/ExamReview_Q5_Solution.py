# Question 5 solution: range(len(word)) because the place matters
word = "committee"
doubles = 0
for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
        doubles += 1
print("Doubles:", doubles)
even = ""
for i in range(len(word)):
    if i % 2 == 0:
        even += word[i]
print("Loop:", even)
print("Slice:", word[::2])
print("Same:", even == word[::2])
