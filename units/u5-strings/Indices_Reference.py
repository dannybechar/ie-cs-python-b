# Unit 5.1 - reference for the teacher. No functions: the class has not learned def yet.
# Each task: a variable with the test value, the code, and print. The file runs top to bottom;
# change a variable's value to try the other test values.


# Warm-up, explained: the last valid index is len(word) - 1 (or -1). word[len(word)] is one past the end:
# IndexError: string index out of range
word = "ROBOT"
last_letter = word[len(word) - 1]
print(last_letter)                             # T   (word[-1] gives the same)

# Task 1: predict-and-check (Ministry worksheet 7.2, questions 1-2)
text1 = "I like to play, "
text2 = "piano"
text3 = "guitar"
print(text1 + text2)                           # I like to play, piano
print(text1 + text3)                           # I like to play, guitar
print(text3 * 2)                               # guitarguitar
msg1 = "abc" + "d" * 3
msg2 = "ef"
msg3 = "7"
print(msg1 + msg2)                             # abcdddef
print(len(msg1))                               # 6
print(len(msg1 + msg2))                        # 8
print(msg3 * 2)                                # 77
print(len(msg3))                               # 1

# Task 2: int() and str() (worksheet question 3) - "+" adds numbers, joins strings
first = "12"
second = "30"
print(int(first) + int(second))                # 42   ("5", "5" -> 10)
print(first + second)                          # 1230 ("5", "5" -> 55)

# Task 3: positive and negative indices on "PYTHON" (worksheet question 4)
text = "PYTHON"
print(text[0])                                 # P
print(text[-6])                                # P
print(text[5])                                 # N
print(text[-1])                                # N
print(text[2])                                 # T
print(text[-4])                                # T    ("ORANGE" -> O O E E A A)

# Task 4: the first letter followed by the last letter
word = "ROBOT"
print(word[0] + word[-1])                      # RT   ("A" -> AA)

# If time: one "*" per character
word = "hello"
print("*" * len(word))                         # *****   ("AI" -> **)
