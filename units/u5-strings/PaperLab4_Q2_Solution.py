# Lessons 8.2-8.7 paper lab - Question 2: ask again until the input is good (type the sample run to check).
username = input("Username: ")
while len(username) < 4:
    print("Too short, try again")
    username = input("Username: ")
print("Hello", username[0].upper())
print("Length:", len(username))
