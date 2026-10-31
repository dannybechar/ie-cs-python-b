# Unit 2.1 - reference for the teacher.
# Classic code: every line of the greeting was written by a person, so the same answers always give the same greeting.
# One function per task. Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: the variable name was typed inside the quotes, so Python printed the word "friend".
# Fix: build the text with + and leave the variable outside the quotes.
def birthday_card():
    friend = input("Friend's name: ")
    print("Happy birthday, " + friend + "!")


# Task 1: two print lines - the output never changes.
def greeting_1():
    print("Happy birthday, Grandma Sarah!")
    print("I wish you health and happiness!")


# Task 2: input + if / else - two possible greetings, written in advance by a person.
def greeting_2():
    sender = input("Who is wishing? (grandson/granddaughter): ")
    print("Happy birthday, Grandma Sarah!")
    if sender == "grandson":
        print("Your grandson wishes you health and happiness!")
    else:
        print("Your granddaughter wishes you health and happiness!")


# Task 3: the hobby is joined into the sentence with + - more personal, but still the same output for the same answers.
def greeting_3():
    sender = input("Who is wishing? (grandson/granddaughter): ")
    hobby = input("What does Grandma Sarah love to do? ")
    print("Happy birthday, Grandma Sarah!")
    print("I wish you lots of joy with " + hobby + "!")
    if sender == "grandson":
        print("Your grandson wishes you health and happiness!")
    else:
        print("Your granddaughter wishes you health and happiness!")


# If time: one more question and one more rule.
def greeting_4():
    sender = input("Who is wishing? (grandson/granddaughter): ")
    hobby = input("What does Grandma Sarah love to do? ")
    age = int(input("How old is Grandma Sarah? "))
    print("Happy birthday, Grandma Sarah!")
    print("I wish you lots of joy with " + hobby + "!")
    if age >= 80:
        print("Eighty years or more of wisdom - what a gift!")
    if sender == "grandson":
        print("Your grandson wishes you health and happiness!")
    else:
        print("Your granddaughter wishes you health and happiness!")


# birthday_card()
# greeting_1()
# greeting_2()
# greeting_3()
greeting_4()
