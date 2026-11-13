# Unit 5.4 paper lab - Question 5: initials in capitals.
band = "red hot chili peppers"

initials = band[0].upper()
for i in range(1, len(band)):
    if band[i - 1] == " ":
        initials += band[i].upper()
print("Initials:", initials)
