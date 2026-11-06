# Unit 5.3 paper lab - Question 2: a ticket code (full solution, plain code, no functions).
code = "TK-2027-AB"

# a. the start, the end and the length
print("Starts with TK-:", code.startswith("TK-"))
print("Ends with a letter:", code[-1].isalpha())
print("Length:", len(code))

# b. how many dashes, and where is the first one
print("Dashes:", code.count("-"))
first = code.find("-")
print("First dash at:", first)

# c. the part between the dashes, and is it a year (four digits)?
rest = code[first + 1:]
second = rest.find("-")
year = rest[:second]
print("Year:", year)
if year.isdigit() and len(year) == 4:
    print("Valid year")
else:
    print("Invalid year")

# d. a cleaned code: no dashes, lower case; and count its digits
cleaned = ""
digits = 0
for ch in code:
    if ch != "-":
        cleaned += ch.lower()
    if ch.isdigit():
        digits += 1
print("Cleaned:", cleaned)
print("Digits:", digits)
