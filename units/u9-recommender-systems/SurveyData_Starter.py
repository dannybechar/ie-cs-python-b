# Warm-up: the last else treats ANY unknown answer (even "v" or "5") as "don't know". Predict, run, then fix it.

def describe_answer(answer):
    if answer == "V":
        return "liked"
    elif answer == "X":
        return "disliked"
    else:
        return "don't know"


print(describe_answer("0"))
print(describe_answer("v"))


# Task 1: write is_valid_answers(answers) - answers is a string such as "VX0XV" (one letter per item).
# Return True if EVERY character is "V", "X" or "0", otherwise False.
# Test: "VX0XV" -> True, "VX0xV" -> False (small x), "VX5XV" -> False.


# Task 2: write count_known(answers) - how many characters are NOT "0" (items the person knows).
# Test: "VX0XV" -> 4.


# Task 3 (if time): write has_all_answers(item_names, answers) - True when the number of answers
# equals the number of items (a row with a missing answer is a broken row).
# Test with item_names = ["sushi", "beet", "dal", "pasta", "pizza"]: "VX0XV" -> True, "VX0X" -> False.
