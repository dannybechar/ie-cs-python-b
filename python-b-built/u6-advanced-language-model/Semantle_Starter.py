# Warm-up: for score 0.70 the meter should show 7 green squares and 3 white ones. Predict, run, then
# fix one line (the two symbols are swapped).


def score_for_display(raw_score):
    return max(0.0, min(1.0, raw_score))


def create_meter(raw_score):
    display_score = score_for_display(raw_score)
    filled = int(display_score * 10)
    empty = 10 - filled
    return "⬜" * filled + "\U0001F7E9" * empty


print(create_meter(0.70))
print(create_meter(0.20))


# CLASSROOM MODE: calculate_similarity() below does not call a real AI model - it is a rule-based
# stand-in (from Unit 6.2) so the file runs with plain Python and needs no downloaded model. Before
# class, swap MOCK_MODE to False and fill in the real model call (see the comment in the reference).

MOCK_MODE = True


# Task 1: complete calculate_similarity(text_a, text_b) so that in classroom mode it returns
# meaning_score_demo(text_a, text_b).
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


def calculate_similarity(text_a, text_b):
    pass  # complete this


def score_to_percent(raw_score):
    return round(score_for_display(raw_score) * 100)


# Task 2 (project - the "semantle" guessing game):
# secret_word = "מוזיקה"; attempts = 0; playing = True.
# While playing: read a guess.
#   - "quit" ends the game.
#   - a guess shorter than 2 characters prints a correction message and does NOT count as an attempt.
#   - otherwise: attempts increases by 1; compute the similarity score and its percent; print the
#     percent and the meter; if the guess equals the secret word exactly, print the number of
#     attempts and end the game.
