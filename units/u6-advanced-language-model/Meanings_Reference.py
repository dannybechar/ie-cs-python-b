# Unit 6.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: compare the character to word_b (a string, checked with "in"),
# not to word_b as a whole (which a single character can never equal).
def shared_letters(word_a, word_b):
    count = 0
    for character in word_a:
        if character in word_b:
            count += 1
    return count


# Not a real AI model - a rule-based stand-in the unit provides, for comparison only.
def meaning_score_demo(guess, target):
    clean_guess = guess.strip().lower()
    clean_target = target.strip().lower()
    if clean_guess == clean_target:
        return 1.0
    elif clean_guess == "פסנתר" and clean_target == "מוזיקה":
        return 0.82
    elif clean_guess == "שיר" and clean_target == "מוזיקה":
        return 0.76
    elif clean_guess == "כדורגל" and clean_target == "מוזיקה":
        return 0.19
    else:
        return 0.35


def compare(word, target="מוזיקה"):
    print(word, "/", target)
    print("  spelling (shared letters):", shared_letters(word, target))
    print("  meaning (demo score):", meaning_score_demo(word, target))


def task():
    compare("פסנתר")
    compare("שיר")
    compare("כדורגל")
    compare("מזוודה")


print(shared_letters("מזוודה", "מוזיקה"))
# task()
