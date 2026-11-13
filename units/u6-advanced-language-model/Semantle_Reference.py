# Unit 6.3 - reference for the teacher (Ministry worksheet 11.3, real model).
# Precondition: Unit 3 (def) is taught first. round() is used for the percent and the bar; the Ministry uses int() - see the lesson notes (checked table).
# Needs: pip install sentence-transformers (the first run downloads the model - do it once before class).
# One task per block; run ONE task at a time by removing the # from its call at the bottom.
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


# Task 1: given to the students (copied from 6.2)
def calculate_similarity(word1, word2):
    meaning_pos1 = model.encode([word1])
    meaning_pos2 = model.encode([word2])
    score_distance = util.cos_sim(meaning_pos1, meaning_pos2).item()
    return score_distance


# Warm-up, fixed: the fire and the snowflake were swapped - a close guess must be mostly fire.
# Extra safety: a cosine score can be slightly below 0, so it is clamped before it builds the bar.
def make_thermometer(score):
    fires = round(20 * max(0.0, min(1.0, score)))
    return "🔥" * fires + "❄️" * (20 - fires)


# Task 2: the basic game - a secret word, a guess loop, the score after every guess
def basic_game():
    secret_word = "אוקינוס"
    guess = ""

    while guess != secret_word:
        guess = input("הכניסו ניחוש: ")
        score = calculate_similarity(secret_word, guess)
        print(score)

    print("סיום")


# Task 3: the attempts counter, shown in the victory message
def game_with_attempts():
    secret_word = "אוקינוס"
    attempts = 0
    guess = ""

    while guess != secret_word:
        attempts += 1
        guess = input("הכניסו ניחוש מספר " + str(attempts) + ": ")
        score = calculate_similarity(secret_word, guess)
        print(score)

    print("כל הכבוד הצלחתם לגלות את המילה הסודית ב", attempts, "ניחושים!")


# Task 4 (project - the checkpoint): the full game with the advanced features
def semantle_game():
    secret_word = "אוקינוס"
    attempts = 0
    guess = ""

    print("-" * 50)
    print("🎮 ברוכים הבאים למשחק סמנטעל! 🎮")
    print("המחשב בחר מילה סודית. נסו לנחש אותה.")
    print("בכל תור תקבלו ציון דמיון מ-0 (קר מאוד) עד 100 (לוהט!).")
    print("-" * 50)

    while guess != secret_word:
        attempts += 1
        guess = input("הכניסו ניחוש מספר " + str(attempts) + ": ")
        score = calculate_similarity(secret_word, guess)
        percent = round(score * 100)
        print("📊 מדחום קירבה: [" + make_thermometer(score) + "] " + str(percent) + "%")

    print()
    print("🏆 כל הכבוד! פיצחתם את המילה הסודית '" + secret_word + "' ב-" + str(attempts) + " ניחושים!")


# Extension (hardening): "quit" ends the game, and a guess shorter than 2 characters is not counted.
def semantle_game_safe():
    secret_word = "אוקינוס"
    attempts = 0
    playing = True

    print("נחשו את המילה הסודית. הקלידו quit ליציאה.")

    while playing:
        guess = input("ניחוש: ").strip()

        if guess == "quit":
            print("המשחק הסתיים.")
            playing = False
        elif len(guess) < 2:
            print("יש להזין לפחות שני תווים.")
        else:
            attempts += 1
            score = calculate_similarity(secret_word, guess)
            print("📊 [" + make_thermometer(score) + "] " + str(round(score * 100)) + "%")
            if guess == secret_word:
                print("ניצחתם לאחר", attempts, "ניסיונות!")
                playing = False


print(make_thermometer(0.70))
print(make_thermometer(0.20))
# basic_game()
# game_with_attempts()
# semantle_game()
# semantle_game_safe()
