# Question 4 solution: for over the characters, "in" for the vowel test, += to build
text = "Education is power"
vowels = 0
rest = ""
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    else:
        rest += ch
print("Vowels:", vowels)
print("Without vowels:", rest)
