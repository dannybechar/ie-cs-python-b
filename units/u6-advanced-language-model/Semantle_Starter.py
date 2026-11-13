# Warm-up: for score 0.70 the thermometer should show 14 fires and 6 snowflakes (a close guess is hot).
# Predict, run, then fix one line (the two symbols are swapped).
# Precondition: Unit 3 (def) is taught first; if not, the teacher hands out calculate_similarity and make_thermometer ready-made.
# Emoji tip: press the Windows key + . (period) to type an emoji; "🔥" * 5 repeats it. Daily Semantle site: TEACHER - add the link (not guessed).
# Needs: pip install sentence-transformers (the first run downloads the model - the teacher does it before class).
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def make_thermometer(score):
    fires = round(20 * score)
    return "❄️" * fires + "🔥" * (20 - fires)


print(make_thermometer(0.70))
print(make_thermometer(0.20))


# Task 1: copy calculate_similarity from your 6.2 file (or from the worksheet) and paste it here.


# Task 2 (basic game): a variable secret_word = "אוקינוס". A loop that keeps asking for a guess until
# the guess equals the secret word. After every guess, print the similarity score between the guess and
# the secret word. When the loop ends, print "סיום".


# Task 3: an attempts counter. Count the guesses and print the number in the victory message:
# "כל הכבוד הצלחתם לגלות את המילה הסודית ב N ניחושים!"


# Task 4 (advanced features - the project):
#   1. show the score as a percentage (score * 100, rounded with round()) with a % sign
#   2. show the closeness as a thermometer: make_thermometer(score) after you fixed it
#   3. a welcome message at the start (what is the game, what is the score) and a victory message at the end
# Optional: "quit" ends the game; a guess shorter than 2 characters is not counted.
