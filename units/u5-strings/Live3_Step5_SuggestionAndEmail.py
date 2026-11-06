# Steps 5-6 (slides 15-17): the suggestion and the e-mail check - the full program
# Run with Pass123 and robot@mail.com; then Moon2026! and robot.mail.com.

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

# ---------- new in this step ----------
# Stage 5 - suggest a stronger password: a -> @, e -> 3, o -> 0, and an exclamation mark at the end
suggestion = ""
for ch in password:
    small = ch.lower()
    if small == "a":
        suggestion += "@"
    elif small == "e":
        suggestion += "3"
    elif small == "o":
        suggestion += "0"
    else:
        suggestion += ch
if not suggestion.endswith("!"):
    suggestion += "!"
print("Suggestion:", suggestion)

# Stage 6 - check an e-mail address: one @, starts with a letter, ends with .com or .co.il
email = input("Email: ")
at = email.find("@")
good = email.count("@") == 1
if good and not email[0].isalpha():
    good = False
com = email.endswith(".com")
il = email.endswith(".co.il")
if good and not (com or il):
    good = False
if good:
    print("Email OK")
    print("User:", email[:at])
    print("Domain:", email[at + 1:])
else:
    print("Email not valid")
