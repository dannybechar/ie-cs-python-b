# Lessons 8.2–8.7 paper lab - Question 5: a number code with dashes, and the total.
word = "snow"

numbers = ""
total = 0
for ch in word:
    place = ord(ch) - 96
    if numbers != "":
        numbers += "-"
    numbers += str(place)
    total += place
print("Number code:", numbers)
print("Total:", total)
