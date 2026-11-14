# Lessons 8.2-8.7 paper lab - challenge: the mirror cipher (a <-> z, b <-> y ...). Plain code, no functions.
text = "Hello World"

# every pair (a, z), (b, y), ... has the same sum of numbers, so the mirror of ch is (sum) - ord(ch)
mirror = ""
for ch in text:
    if ch.isalpha():
        if ch == ch.lower():
            mirror += chr(ord("a") + ord("z") - ord(ch))
        else:
            mirror += chr(ord("A") + ord("Z") - ord(ch))
    else:
        mirror += ch
print("Mirror:", mirror)

# the mirror of the mirror is the original: run the same steps on the result
back = ""
for ch in mirror:
    if ch.isalpha():
        if ch == ch.lower():
            back += chr(ord("a") + ord("z") - ord(ch))
        else:
            back += chr(ord("A") + ord("Z") - ord(ch))
    else:
        back += ch
print("Back:", back)
if back == text:
    print("Same: yes")
else:
    print("Same: no")
