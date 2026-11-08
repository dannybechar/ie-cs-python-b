# Unit 6.2 - reference for the teacher (Ministry worksheet 11.2, real model).
# Needs: pip install sentence-transformers (the first run downloads the model - do it once before class).
# One task per block; run ONE task at a time by removing the # from its call at the bottom.
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


# Warm-up, fixed: compare the character to word_b (a string, checked with "in"),
# not to word_b as a whole (which a single character can never equal).
def shared_letters(word_a, word_b):
    count = 0
    for character in word_a:
        if character in word_b:
            count += 1
    return count


# Task 1: the similarity function (the names the students fill in)
def calculate_similarity(word1, word2):
    # the model turns each word into its "address" on the meaning map
    meaning_pos1 = model.encode([word1])
    meaning_pos2 = model.encode([word2])
    # the distance between the two addresses; closer to 1 = closer in meaning
    score_distance = util.cos_sim(meaning_pos1, meaning_pos2).item()
    return score_distance


# Task 2: a program that reads two words, prints the score and a verdict
def task2():
    word1 = input("הכנס מילה ראשונה: ")
    word2 = input("הכנס מילה שנייה: ")

    score = calculate_similarity(word1, word2)
    print("הציון של", word1, "ו-" + word2, "הוא:", score)

    if score >= 0.5:
        print("המילים האלו קרובות במשמעות!")
    elif score > 0.3:
        print("יש קשר מסוים")
    else:
        print("המילים האלו מעולמות שונים לחלוטין")


# Task 3: spelling vs meaning, against "מוזיקה" (real scores, rounded)
def compare(word, target="מוזיקה"):
    print(word, "/", target)
    print("  spelling (shared letters):", shared_letters(word, target))
    print("  meaning (model score):", round(calculate_similarity(word, target), 2))


def task3():
    compare("פסנתר")
    compare("שיר")
    compare("כדורגל")
    compare("מזוודה")


# Task 4: the playground (the scores in the comments are from a real run; yours may differ slightly)
def playground():
    print("שפות:", round(calculate_similarity("computer", "מחשב"), 3))       # 0.994
    print("הפכים:", round(calculate_similarity("happy", "sad"), 3))          # 0.614
    print("לא קשורות:", round(calculate_similarity("london", "monkey"), 3))  # 0.172
    print("מותגים:", round(calculate_similarity("McDonald's", "Burger King"), 3))  # 0.64


print(shared_letters("מזוודה", "מוזיקה"))
# task2()
# task3()
# playground()
