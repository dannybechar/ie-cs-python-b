# Unit 5.4 - reference for the teacher.
# Warm-up, then the "Smart Text Checker" project - the unit checkpoint.


# Warm-up, explained: count_letters() was copy-pasted from count_digits() and never updated -
# it still checks isnumeric() instead of isalpha(). A common bug: copying a function and
# forgetting to change the one line that made it a different job.
def normalize(text):
    return text.strip().lower()


def count_digits(text):
    total = 0
    for character in text:
        if character.isnumeric():
            total += 1
    return total


def count_letters(text):
    total = 0
    for character in text:
        if character.isalpha():
            total += 1
    return total


def count_spaces(text):
    total = 0
    for character in text:
        if character == " ":
            total += 1
    return total


def hide_digits(text):
    result = ""
    for character in text:
        if character.isnumeric():
            result += "#"
        else:
            result += character
    return result


def make_preview(text, limit):
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def build_report(text):
    clean = normalize(text)
    print("Length:", len(text))
    print("Letters:", count_letters(text))
    print("Digits:", count_digits(text))
    print("Spaces:", count_spaces(text))
    print("Contains maybe:", "maybe" in clean)
    print("Starts with summary:", clean.startswith("summary:"))
    print("Preview:", make_preview(text, 40))
    print("Hidden digits:", hide_digits(text))


# Project - the checkpoint
def smart_text_checker():
    text = input("Paste a prompt or an AI answer: ")
    build_report(text)


build_report("SUMMARY: Maybe 3 examples are enough.")
# smart_text_checker()
