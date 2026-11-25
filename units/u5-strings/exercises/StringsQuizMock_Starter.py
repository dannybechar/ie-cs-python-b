# Mock quiz - strings block. Solve on paper first, then type your answers here and run.
# Q1: check every line of part a and part b. Q2: run the buggy code, then fix it.

# --- Q1 ---
word = "elephant"
print(word[1:4])
print(word[-3:])
print(word[::2])
print(word.find("ph"))
print("ha" in word)
print(word.replace("e", "E"))

word = "elephant"
word.upper()
print(word)

# --- Q2 a (crashes: find the error, then fix) ---
name = "Daniel"
print("Last letter:", name[len(name)])

# --- Q2 b (wrong output: fix so it prints na na na) ---
song = "la la la"
song.replace("la", "na")
print(song)

# --- Q3: write your code here ---
code = "ab-2045-xy"

# --- Q4: write your three pieces of code here ---
sentence = "Strings are fun"
