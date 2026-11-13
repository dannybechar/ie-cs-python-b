# Warm-up: shared_letters should count how many letters of word_a also appear in word_b (spelling,
# not meaning). Predict a positive number for the pair below, run, then fix one comparison.
# Precondition: Unit 3 (def) is taught first; if not, the teacher hands out calculate_similarity ready-made (students only call it).
# Note: model.encode([word]) - the square brackets are copied as written (the library asks for a list; lists are taught in Unit 7).
# Needs: pip install sentence-transformers (the first run downloads the model - the teacher does it before class).
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def shared_letters(word_a, word_b):
    count = 0
    for character in word_a:
        if character == word_b:
            count += 1
    return count


print(shared_letters("מזוודה", "מוזיקה"))


# Task 1: complete the function - replace every ___ with a variable name (word1, word2, meaning_pos1, meaning_pos2, score_distance).
def calculate_similarity(word1, word2):
    # the model turns the first word into its "address" on the meaning map
    meaning_pos1 = model.encode([___])        # <- replace ___ with the right variable
    # the same for the second word
    meaning_pos2 = model.encode([___])        # <- and here
    # the distance between the two addresses
    score_distance = util.cos_sim(___, ___).item()   # <- and here (two variables)
    # the closer to 1, the closer in meaning
    return ___                                # <- what do we return?


# Task 2: write a program that reads two words, prints the score between them, and then prints:
#   score >= 0.5            -> "המילים האלו קרובות במשמעות!"
#   score between 0.3 and 0.5 -> "יש קשר מסוים"
#   score <= 0.3            -> "המילים האלו מעולמות שונים לחלוטין"


# Task 3: for each word below print its spelling score against "מוזיקה" (shared_letters) and its
# meaning score (calculate_similarity), then write one sentence about what the comparison shows:
#   פסנתר, שיר, כדורגל, מזוודה


# Task 4 - the playground (explore; it is fine not to solve everything):
#   1. language test: the same word in Hebrew and English (dog / כלב)
#   2. opposites test: happy / sad - far or close?
#   3. unrelated words: the pair closest to 0 you can find in 10 tries
#   4. brands: two brands from the same world (adidas / nike)
