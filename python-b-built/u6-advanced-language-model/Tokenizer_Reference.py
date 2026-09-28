# Unit 6.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: the loop never flushes a token still sitting in `current` when the text ends.
# Add the same flush after the loop that already happens inside it.
def simple_tokenize(text):
    result = ""
    current = ""

    for character in text:
        if character.isalpha() or character.isnumeric():
            current += character.lower()
        else:
            if current != "":
                result += "[" + current + "]"
                current = ""
            if character != " ":
                result += "[" + character + "]"

    if current != "":
        result += "[" + current + "]"

    return result


# Task 1: spaces become their own [SPACE] token
def simple_tokenize_with_spaces(text):
    result = ""
    current = ""

    for character in text:
        if character.isalpha() or character.isnumeric():
            current += character.lower()
        else:
            if current != "":
                result += "[" + current + "]"
                current = ""
            if character == " ":
                result += "[SPACE]"
            else:
                result += "[" + character + "]"

    if current != "":
        result += "[" + current + "]"

    return result


# Task 2: count tokens by counting how many were opened
def token_count(text):
    return simple_tokenize(text).count("[")


def task2():
    print(token_count("hello"))
    print(token_count("hello!"))
    print(token_count("ice cream"))
    print(token_count("icecream"))


print(simple_tokenize("AI helps, sometimes!"))
print(simple_tokenize_with_spaces("AI helps"))
# task2()
