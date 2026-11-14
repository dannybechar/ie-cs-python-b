# Warm-up: tokens_sentence should print the token IDs of the sentence. Predict, run, then fix one line.
# Precondition: the functions block (lessons 4.1–4.6) (def) is taught first; if not, the teacher hands out the three functions ready-made and students only call them.
# Needs: pip install sentence-transformers (the first run downloads the model - the teacher does it before class).
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
tokenizer = model.tokenizer

sentence = "אני אוהב ללמוד פייתון בבית הספר"


def tokens_sentence(sentence):
    tokens = tokenizer.tokenize(sentence)
    print("tokens:", tokens)
    token_ids = tokenizer.convert_tokens_to_ids(sentence)
    print("token_ids:", token_ids)
    return tokens


tokens_sentence(sentence)


# Task 1: write print_sentence_info(sentence) - prints the length of the sentence in characters
# and the number of spaces in it. Call it on the sentence above.


# Task 2: (after the warm-up) look at the tokens. Are they whole words? Which ones are parts of words?


# Task 3: write count_tokens(text) - returns how many tokens the tokenizer made from text.


# Task 4 - the playground (no need to program more; just play with count_tokens and tokenizer.tokenize):
#   1. How many tokens is your name, in English and in Hebrew?
#   2. Challenge: in 10 tries, find a Hebrew sentence with FEWER tokens than the same sentence in English.
#   3. A word of 5 letters that breaks into the most tokens - try 10 words (what is your record?).
#   4. Is "apple" the same as "APPLE"? Compare the token IDs.
