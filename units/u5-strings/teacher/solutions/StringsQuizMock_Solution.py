# Mock quiz (practice) - strings block. Full solutions, plain code, no functions.
print("=== Q1 a ===")
word = "elephant"
print(word[1:4])
print(word[-3:])
print(word[::2])
print(word.find("ph"))
print("ha" in word)
print(word.replace("e", "E"))
print("=== Q1 b ===")
word = "elephant"
word.upper()
print(word)

print("=== Q2 a (bug: IndexError) ===")
name = "Daniel"
print("Last letter:", name[len(name) - 1])
print("=== Q2 b (bug: replace not saved) ===")
song = "la la la"
song = song.replace("la", "na")
print(song)

print("=== Q3 ===")
code = "ab-2045-xy"
place = code.find("-")
print("Prefix:", code[:place])
print("Rest:", code[place + 1:])
print("Upper:", code.upper())
print("Dashes:", code.count("-"))
print("Has 2045:", "2045" in code)

print("=== Q4 ===")
sentence = "Strings are fun"
count = 0
for ch in sentence:
    if ch.lower() == "s":
        count += 1
print("S count:", count)
new = ""
for ch in sentence:
    if ch == "n":
        new += "*"
    else:
        new += ch
print("Stars:", new)
for i in range(len(sentence)):
    if sentence[i] == "r":
        print("Place:", i)
