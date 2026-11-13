# Unit 5.4 paper lab - Question 2: count the words (the spaces plus one).
sentence = "the quick brown fox jumps"

words = sentence.count(" ") + 1
print("Words:", words)
if words > 4:
    print("Long sentence")
else:
    print("Short sentence")
