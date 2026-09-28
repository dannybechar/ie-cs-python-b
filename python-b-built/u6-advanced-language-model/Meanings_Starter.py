# Warm-up: this should measure how similar two words LOOK (their spelling), not what they mean.
# Predict, run, then fix one comparison.


def shared_letters(word_a, word_b):
    count = 0
    for character in word_a:
        if character == word_b:
            count += 1
    return count


print(shared_letters("מזוודה", "מוזיקה"))


# The function below is NOT a real AI model - it is a rule-based stand-in the unit provides,
# with a few fixed answers (all about the target word "מוזיקה") and one default for everything else.
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


# Task: for each word below, print its spelling score against "מוזיקה" (shared_letters) and its
# meaning score (meaning_score_demo), then write one sentence explaining what the comparison shows.
#   פסנתר   - 0 shared letters, but the demo scores it close in meaning (0.82)
#   שיר     - 1 shared letter, still scored close in meaning (0.76)
#   כדורגל  - 1 shared letter, scored far in meaning (0.19)
#   מזוודה  - 5 shared letters (spelling looks close!), but no special meaning rule for it
