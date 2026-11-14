# Lessons 7.1–7.2 paper lab - Question 1: a file name (full solution, plain code, no functions).
file = "holiday_photo_2026.jpg"

# a. the name without the extension, and the extension
dot = file.find(".")
print("Name:", file[:dot])
print("Extension:", file[dot + 1:])

# b. count the underscores and find the first one
count = file.count("_")
print("Underscores:", count)
print("First at:", file.find("_"))

# c. replace every underscore with a space; then only the first one with a dash
print(file.replace("_", " "))
print(file.replace("_", "-", 1))

# d. a message if there is no underscore, otherwise the place of every underscore
if count == 0:
    print("No underscore")
else:
    for i in range(len(file)):
        if file[i] == "_":
            print("Underscore at", i)
