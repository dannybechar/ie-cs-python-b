# Lessons 8.2–8.7 paper lab - Question 3: the number of words and the initials in capitals.
band = "red hot chili peppers"

words = band.count(" ") + 1
initials = band[0].upper()
for i in range(1, len(band)):
    if band[i - 1] == " ":
        initials += band[i].upper()
print("Words:", words)
print("Initials:", initials)
