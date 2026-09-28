# Warm-up: this simple tokenizer should print [ai][helps] for "AI helps". Predict, run, then fix one thing.


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

    return result


print(simple_tokenize("AI helps"))


# Task 1: extend simple_tokenize (call it simple_tokenize_with_spaces) so every space also becomes
# its own token, written as [SPACE].


# Task 2: write token_count(text) - returns how many tokens simple_tokenize produced for text
# (count how many "[" characters are in the result). Use it to compare a few short texts.
