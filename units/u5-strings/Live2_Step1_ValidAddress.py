# Step 1 (slides 8-9): a valid address with find, count and while
# Run: type dana (rejected), x@school.org (rejected), then noam@school.org.

# Stage 1 - read an address; it needs exactly one @ and at least 2 characters before it
email = input("Email: ")
while email.count("@") != 1 or email.find("@") < 2:
    print("Invalid address")
    email = input("Email: ")
print("Length:", len(email))
