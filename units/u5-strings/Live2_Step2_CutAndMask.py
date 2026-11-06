# Step 2 (slides 5-7 and 10-11): cut the address with slices; mask, reverse, every second letter
# Run with noam@school.org.

# Stage 1 - read an address; it needs exactly one @ and at least 2 characters before it
email = input("Email: ")
while email.count("@") != 1 or email.find("@") < 2:
    print("Invalid address")
    email = input("Email: ")
print("Length:", len(email))

# ---------- new in this step ----------
# Stage 2 - cut the address into the user and the domain
at = email.find("@")
user = email[:at]
domain = email[at + 1:]
print("User:", user)
print("Domain:", domain)
print("Ending:", email[-3:])

# Stage 3 - slices with a jump: mask the user, reverse it, every second letter
masked = user[0] + "*" * (len(user) - 2) + user[-1]
print("Masked:", masked)
print("Backwards:", user[::-1])
print("Every second:", user[::2])
