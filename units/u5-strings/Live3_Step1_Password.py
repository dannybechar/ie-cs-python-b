# Step 1 (slides 5-8): the password and a weak pattern
# Run: type abc (too short), then Pass123.

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
