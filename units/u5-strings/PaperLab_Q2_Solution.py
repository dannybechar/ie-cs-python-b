# Unit 5.1 paper lab - Question 2: registering a user (full solution, plain code, no functions).

# a. a username of 4 to 10 characters; ask again until it is valid
username = input("Username: ")
while len(username) < 4 or len(username) > 10:
    print("Must be 4 to 10 characters")
    username = input("Username: ")

# b. the masked name: the first letter, then a star for each of the other letters
print("Masked: " + username[0] + "*" * (len(username) - 1))

# c. an age of 1 to 120; ask again until it is valid, then next year's age
age = int(input("Age: "))
while age < 1 or age > 120:
    print("Age must be 1 to 120")
    age = int(input("Age: "))
print("Next year you will be", age + 1)

# d. a framed card; the frame fits the longer of the two lines
line1 = username
line2 = "Age: " + str(age)
width = len(line1)
if len(line2) > width:
    width = len(line2)
border = "*" * (width + 4)
gap1 = " " * (width - len(line1))
gap2 = " " * (width - len(line2))
print(border)
print("* " + line1 + gap1 + " *")
print("* " + line2 + gap2 + " *")
print(border)
