# Unit 5.4 paper lab - Question 6: count vowels and consonants.
word = "education"

vowels = 0
for ch in word:
    if ch in "aeiou":
        vowels += 1
print("Vowels:", vowels)
print("Consonants:", len(word) - vowels)
