# Reference solutions for the Unit 5.3 paper classwork (Ministry 8.0 / 8.1: walking over a string with for).
# One function per task. Run this file to see every answer next to the value the worksheet expects.


# --- Part A: read the code, predict on paper, then run ---------------------------------------------

def a1_comma_print():
    for ch in "sometimes":
        print(ch, end=",")
    print()                                  # ends the line


def a2_keep_a_to_e():
    new_text = ""
    for ch in "We play on the computer":
        if ch >= "a" and ch <= "e":
            new_text = new_text + ch
    print(new_text)


def a3_count_words():
    sentence = "We are learning to program"
    count = 0
    for ch in sentence:
        if ch == " ":
            count += 1
    print(sentence)
    print("Number of words:", count + 1)


def a4_trace_banana():
    count = 0
    for ch in "banana":
        if ch == "a":
            count += 1
    return count


# --- Part B: write the function on paper, then type it ----------------------------------------------

def count_letter(text, letter):              # B1: the fixed warm-up bug
    count = 0                                # once, BEFORE the loop
    for ch in text:
        if ch == letter:
            count += 1
    return count


def count_char(text, letter):                # B2 (Ministry exercise 1)
    count = 0
    for ch in text:
        if ch == letter:
            count += 1
    return count


def triple_print(text):                      # B3 (Ministry exercise 2), printing version
    for ch in text:
        print(ch * 3, end="")
    print()


def triple(text):                            # B3, returning version
    result = ""
    for ch in text:
        result += ch * 3
    return result


def count_letters(text):                     # B4
    count = 0
    for ch in text:
        if ch.isalpha():
            count += 1
    return count


def count_digits(text):                      # B4
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
    return count


def count_spaces(text):                      # B4
    count = 0
    for ch in text:
        if ch == " ":
            count += 1
    return count


def count_vowels(text):                      # B5 (Ministry exercise 7, one total)
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


# --- Homework / if time -----------------------------------------------------------------------------

def only_digits(text):                       # B6
    digits = ""
    for ch in text:
        if ch.isdigit():
            digits += ch
    return digits


def hide_digits(text):                       # B7
    hidden = ""
    for ch in text:
        if ch.isdigit():
            hidden += "*"
        else:
            hidden += ch
    return hidden


def count_each_vowel(text):                  # challenge (Ministry exercise 7, five counters)
    a = e = i = o = u = 0
    for ch in text.lower():
        if ch == "a":
            a += 1
        elif ch == "e":
            e += 1
        elif ch == "i":
            i += 1
        elif ch == "o":
            o += 1
        elif ch == "u":
            u += 1
    print("a:", a, "e:", e, "i:", i, "o:", o, "u:", u)


AI_ANSWER = "The Moon orbits the Earth. It takes about 27 days. Some answers are wrong, so we check."


def check_ai_answer(answer):                 # B8: what a loop can count, and what it cannot judge
    print("Sentences (dots):", count_char(answer, "."))
    print("Words (spaces + 1):", count_spaces(answer) + 1)
    print("Digits:", count_digits(answer))


def check(label, got, expected):
    print(("OK   " if got == expected else "FAIL ") + label, "->", repr(got))


if __name__ == "__main__":
    print("A1:"); a1_comma_print()
    print("A2:"); a2_keep_a_to_e()
    print("A3:"); a3_count_words()
    check("A4 banana", a4_trace_banana(), 3)
    sentence = "sometimes you win sometimes you learn"
    check("B1", count_letter(sentence, "e"), 5)
    check("B2 e", count_char(sentence, "e"), 5)
    check("B2 banana a", count_char("banana", "a"), 3)
    check("B2 banana x", count_char("banana", "x"), 0)
    check("B2 empty", count_char("", "a"), 0)
    check("B3 triple", triple("Learn"), "LLLeeeaaarrrnnn")
    print("B3 triple_print:"); triple_print("Learn")
    ai = "In 2024 the model answered 3 questions."
    check("B4 letters", count_letters(ai), 27)
    check("B4 digits", count_digits(ai), 5)
    check("B4 spaces", count_spaces(ai), 6)
    check("B5 Hello World", count_vowels("Hello World"), 3)
    check("B5 rhythm", count_vowels("rhythm"), 0)
    check("B5 AEIOU", count_vowels("AEIOU"), 5)
    check("B5 empty", count_vowels(""), 0)
    check("B6", only_digits("In 2027 I turn 15"), "202715")
    check("B7", hide_digits("Room 12 floor 3"), "Room ** floor *")
    print("Challenge:"); count_each_vowel("Education is the key")
    print("B8:"); check_ai_answer(AI_ANSWER)
