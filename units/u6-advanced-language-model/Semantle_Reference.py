# Unit 6.3 - reference for the teacher.
# CLASSROOM MODE: calculate_similarity() calls a stand-in, not a real model, so this file runs with
# plain Python and needs no download. Before class, swap MOCK_MODE to False and fill in the real
# model call below - then test it live in Thonny with the model installed and downloaded once.

MOCK_MODE = True


# Warm-up, fixed: the fill color and the empty color were swapped.
def score_for_display(raw_score):
    return max(0.0, min(1.0, raw_score))


def create_meter(raw_score):
    display_score = score_for_display(raw_score)
    filled = int(display_score * 10)
    empty = 10 - filled
    return "\U0001F7E9" * filled + "⬜" * empty


# Not a real AI model - the same rule-based stand-in from Unit 6.2, reused here.
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


# Task 1: calculate_similarity, completed
def calculate_similarity(text_a, text_b):
    if MOCK_MODE:
        return meaning_score_demo(text_a, text_b)

    # Real model (needs `pip install -U sentence-transformers`; the first download is large -
    # do it once, before class, not during):
    #
    # from sentence_transformers import SentenceTransformer, util
    # MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    # model = SentenceTransformer(MODEL_NAME)  # load ONCE, outside this function and outside any loop
    # embeddings = model.encode([text_a, text_b], convert_to_tensor=True)
    # return float(util.cos_sim(embeddings[0], embeddings[1]).item())
    raise NotImplementedError("Fill in the real model above and set MOCK_MODE = False.")


def score_to_percent(raw_score):
    return round(score_for_display(raw_score) * 100)


# Task 2 (project - the checkpoint): the semantic guessing game
def semantle_game():
    secret_word = "מוזיקה"
    attempts = 0
    playing = True

    print("נחשו את המילה הסודית. הקלידו quit ליציאה.")

    while playing:
        guess = input("ניחוש: ").strip().lower()

        if guess == "quit":
            print("המשחק הסתיים.")
            playing = False
        elif len(guess) < 2:
            print("יש להזין לפחות שני תווים.")
        else:
            attempts += 1
            score = calculate_similarity(guess, secret_word)
            percent = score_to_percent(score)

            print("קרבה:", percent, "%")
            print(create_meter(score))

            if guess == secret_word:
                print("ניצחתם לאחר", attempts, "ניסיונות!")
                playing = False
            elif percent >= 75:
                print("חם מאוד")
            elif percent >= 50:
                print("מתקרבים")
            else:
                print("עדיין רחוק")


print(create_meter(0.70))
print(create_meter(0.20))
# semantle_game()
