# Unit 5.4 - countdown cases, reference for the teacher.
# Every case is solved twice: once with a for loop, once with a while loop, using a DIFFERENT idea.
# The countdown page shows both on the reveal screen (it is built from this file).


# Case 1: how many times does "is" appear? (Ministry exercise 6, without count)
# for: check every place in the text - does a two-letter slice equal "is"?
def count_is_for(text):
    total = 0
    for index in range(len(text) - 1):
        if text[index:index + 2] == "is":
            total += 1
    return total


# while: jump straight to the next "is" with find(..., start) until find says -1
def count_is_while(text):
    total = 0
    place = text.find("is")
    while place != -1:
        total += 1
        place = text.find("is", place + 1)
    return total


# Case 2: the first letter of every word (Ministry exercise 5)
# for: walk over the characters and remember the previous one in a variable
def initials_for(text):
    result = ""
    previous = " "
    for character in text:
        if previous == " " and character != " ":
            result += character
        previous = character
    return result


# while: walk over the places and look back at text[index - 1]
def initials_while(text):
    if text == "":
        return ""
    result = text[0]
    index = 1
    while index < len(text):
        if text[index - 1] == " ":
            result += text[index]
        index += 1
    return result


# Case 3: the next-letter cipher with ord and chr (lower-case text; z becomes a; a space stays)
# for: a special case for "z"
def next_letters_for(text):
    result = ""
    for character in text:
        if character == "z":
            result += "a"
        elif character.isalpha():
            result += chr(ord(character) + 1)
        else:
            result += character
    return result


# while: no special case - count the place in the alphabet (0-25), add 1, and % 26 wraps 26 back to 0
def next_letters_while(text):
    result = ""
    index = 0
    while index < len(text):
        character = text[index]
        if character.isalpha():
            place = ord(character) - ord("a")
            place = (place + 1) % 26
            result += chr(ord("a") + place)
        else:
            result += character
        index += 1
    return result


# Case 4: the first word and the last word (Ministry exercise 4)
# for: walk over the whole text and remember the LAST space seen
def first_and_last_word_for(text):
    first_space = text.find(" ")
    if first_space == -1:
        return text
    last_space = first_space
    for index in range(len(text)):
        if text[index] == " ":
            last_space = index
    return text[:first_space] + " " + text[last_space + 1:]


# while: start at the end and walk back until the first space you meet
def first_and_last_word_while(text):
    first_space = text.find(" ")
    if first_space == -1:
        return text
    index = len(text) - 1
    while text[index] != " ":
        index -= 1
    return text[:first_space] + " " + text[index + 1:]


print("Case 1:", count_is_for("this is his list"), count_is_while("this is his list"), "expected 4")
print("Case 1:", count_is_for("Mississippi is big"), count_is_while("Mississippi is big"), "expected 3")
print("Case 2:", initials_for("American Standard Code Information Interchange"),
      initials_while("American Standard Code Information Interchange"), "expected ASCII")
print("Case 2:", initials_for("grade eight python"), initials_while("grade eight python"), "expected gep")
print("Case 3:", next_letters_for("abcd"), next_letters_while("abcd"), "expected bcde")
print("Case 3:", next_letters_for("zoo"), next_letters_while("zoo"), "expected app")
print("Case 3:", next_letters_for("i like python"), next_letters_while("i like python"), "expected j mjlf qzuipo")
print("Case 4:", first_and_last_word_for("Cats and dogs are great friends"),
      "/", first_and_last_word_while("Cats and dogs are great friends"), "expected Cats friends")
print("Case 4:", first_and_last_word_for("Hello"), first_and_last_word_while("Hello"), "expected Hello")
