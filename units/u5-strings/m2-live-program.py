# Unit 5.2 live program: the Email Desk - full solution.
# The program is built in six stages; each stage adds lines and the program still runs.

# Stage 1 - read an address; it needs exactly one @ and at least 2 characters before it
email = input("Email: ")
while email.count("@") != 1 or email.find("@") < 2:
    print("Invalid address")
    email = input("Email: ")
print("Length:", len(email))

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

# Stage 4 - look inside the domain: find, count and replace
dot = domain.find(".")
if dot == -1:
    print("The domain has no dot")
else:
    print("Site:", domain[:dot])
    print("Tail:", domain[dot + 1:])
print("Dots:", domain.count("."))
spoken = email.replace("@", " at ")
spoken = spoken.replace(".", " dot ")
print("Spoken:", spoken)

# Stage 5 - slices inside loops: growing prefixes and rotations of the user
for i in range(len(user)):
    print(user[:i + 1])
for i in range(len(user)):
    print(user[i:] + user[:i])

# Stage 6 - the card: masked address and the type, framed to the longer line
line1 = masked + "@" + domain
if "school" in domain:
    line2 = "Type: school"
else:
    line2 = "Type: other"
width = len(line1)
if len(line2) > width:
    width = len(line2)
border = "*" * (width + 4)
gap1 = " " * (width - len(line1))
gap2 = " " * (width - len(line2))
print(border)
print("* " + line1 + gap1 + " *")
print("* " + line2 + gap2 + " *")
print(border)
