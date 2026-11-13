# Unit 5.4 paper lab - Question 8: a number code with dashes, and the total.
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
