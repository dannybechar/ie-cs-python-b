# Warm-up: build_report() should print a full report, but the header count is wrong. Predict, run, fix.


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
        if character.isnumeric():
            total += 1
    return total


def build_report(text):
    clean = normalize(text)
    print("Length:", len(text))
    print("Letters:", count_letters(text))
    print("Digits:", count_digits(text))
    print("Has maybe:", "maybe" in clean)


build_report("SUMMARY: Maybe 3 examples are enough.")


# Project - "Smart Text Checker": a program that reads a prompt or AI answer and prints:
#   - a normalized version (stripped, lowercase) - not printed on its own, but used for checks
#   - total length
#   - count of letters, digits, and spaces
#   - how many times "maybe" appears (case-insensitive)
#   - whether the text starts with "summary:" (after normalizing)
#   - a preview of up to 40 characters, ending in "..." only if the text was cut
#   - a version with every digit hidden as "#"
#
# Build it as small functions, each taking text and returning one result - normalize, count_digits,
# count_letters, count_spaces, hide_digits, make_preview. Test with at least: a normal sentence, an
# empty string, a short text (under 40 characters), a long text (over 40), and a header that starts
# with "SUMMARY:".
