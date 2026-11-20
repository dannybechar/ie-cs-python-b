# Question 2 solution: find the "@", then slice before and after it
email = "dana@school.org"
at = email.find("@")
name = email[:at]
domain = email[at + 1:]
print("Name:", name)
print("Domain:", domain)
print("Name in capitals:", name.upper())
print("Has school:", "school" in email)
