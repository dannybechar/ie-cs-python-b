# Lessons 10.0–10.2 - reference for the teacher (Ministry worksheet 10.2, real tokenizer).
# Needs: pip install sentence-transformers (the first run downloads the model - do it once before class).
# One task per block; run ONE task at a time by removing the # from its call at the bottom.
# Precondition: the functions block (lessons 4.1–4.6) (def) is taught first. If not, hand the three functions to the students ready-made.
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
tokenizer = model.tokenizer

sentence = "אני אוהב ללמוד פייתון בבית הספר"


# Task 1: characters and spaces
def print_sentence_info(sentence):
    print("אורך המשפט (תווים):", len(sentence))
    print("מספר רווחים:", sentence.count(" "))


# Task 2, warm-up fixed: convert_tokens_to_ids needs the LIST OF TOKENS, not the sentence.
# Given the sentence as a string, it treats the whole sentence as one unknown token.
def tokens_sentence(sentence):
    tokens = tokenizer.tokenize(sentence)
    print("tokens:", tokens)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    print("token_ids:", token_ids)
    return tokens


# Task 3: how many tokens?
def count_tokens(text):
    return len(tokenizer.tokenize(text))


# Task 4: the playground (four experiments)
def playground():
    print("1. השם שלי:", count_tokens("Danny Bechar"), "|", count_tokens("דן בכר"))
    print("   השם בדף הפתרון של המשרד: עפרי =", count_tokens("עפרי"), "טוקנים")
    print("2. משפט בעברית עם פחות טוקנים מאנגלית (אתגר - 10 ניסיונות):")
    print("   hello world =", count_tokens("hello world"), "| שלום עולם =", count_tokens("שלום עולם"))
    print("   (הזוג הארוך: עברית", count_tokens("אני אוהב ללמוד פייתון בבית הספר"),
          "אנגלית", count_tokens("I love learning Python at school"), ")")
    print("3. מילה בת 5 אותיות:")
    print("  ", "qxzjw", count_tokens("qxzjw"), tokenizer.tokenize("qxzjw"))
    print("  ", "פצצצץ", count_tokens("פצצצץ"), tokenizer.tokenize("פצצצץ"))
    print("  ", "ארצנו", count_tokens("ארצנו"), tokenizer.tokenize("ארצנו"), "(הדוגמה של המשרד: 3)")
    print("  ", "Mississippi", count_tokens("Mississippi"), tokenizer.tokenize("Mississippi"))
    print("4. אותיות גדולות:")
    print("  ", tokenizer.tokenize("apple"), tokenizer.convert_tokens_to_ids(tokenizer.tokenize("apple")))
    print("  ", tokenizer.tokenize("APPLE"), tokenizer.convert_tokens_to_ids(tokenizer.tokenize("APPLE")))


# Extension (if time): our own toy tokenizer, to compare with the real one.
# Warm-up bug of the old version, fixed: flush `current` after the loop.
def simple_tokenize(text):
    result = ""
    current = ""

    for character in text:
        if character.isalpha() or character.isnumeric():
            current += character.lower()
        else:
            if current != "":
                result += "[" + current + "]"
                current = ""
            if character != " ":
                result += "[" + character + "]"

    if current != "":
        result += "[" + current + "]"

    return result


print_sentence_info(sentence)
tokens_sentence(sentence)
# print(count_tokens("hello world"), count_tokens("שלום עולם"))
# playground()
# print(simple_tokenize("AI helps, sometimes!"))
