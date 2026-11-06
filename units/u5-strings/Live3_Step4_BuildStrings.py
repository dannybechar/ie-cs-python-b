# Step 4 (slide 14): build new strings with +=
# Run with Pass123.

# Stage 1 - read the password (at least 6 characters) and look for a weak pattern
password = input("Password: ")
while len(password) < 6:
    print("Too short, try again")
    password = input("Password: ")
lowered = password.lower()
weak = False
if lowered.startswith("pass"):
    weak = True
if lowered.endswith("123"):
    weak = True
if weak:
    print("Weak pattern found")

# Stage 2 - walk over the characters and count each kind
letters = 0
digits = 0
upper = 0
symbols = 0
for ch in password:
    if ch.isalpha():
        letters += 1
        if ch == ch.upper():
            upper += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1
print("Letters:", letters)
print("Digits:", digits)
print("Upper-case:", upper)
print("Symbols:", symbols)

# Stage 3 - a score out of 5 and a rating
score = 0
if len(password) >= 8:
    score += 1
if digits > 0:
    score += 1
if upper > 0:
    score += 1
if symbols > 0:
    score += 1
if not weak:
    score += 1
print("Score:", score, "out of 5")
if score >= 4:
    print("Rating: Strong")
elif score >= 2:
    print("Rating: Medium")
else:
    print("Rating: Weak")

# ---------- new in this step ----------
# Stage 4 - build new strings with += : letters only, digits only, swapped case
only_letters = ""
only_digits = ""
swapped = ""
for ch in password:
    if ch.isalpha():
        only_letters += ch
    if ch.isdigit():
        only_digits += ch
    if ch == ch.upper():
        swapped += ch.lower()
    else:
        swapped += ch.upper()
print("Letters only:", only_letters)
print("Digits only:", only_digits)
print("Swapped case:", swapped)
