# Step 2 (slides 9-12): walk over the characters and count each kind
# Run with Pass123; then Moon2026!

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

# ---------- new in this step ----------
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
