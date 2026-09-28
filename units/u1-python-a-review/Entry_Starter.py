# Warm-up: this program crashes. Run it with age 10 and 2 tickets, read the error, then fix one line.
# Children under 12 pay 8 per ticket; everyone else pays 12.


def ticket_price():
    age = input("Age: ")
    tickets = int(input("Tickets: "))
    if age < 12:
        price = 8
    else:
        price = 12
    print("Total:", tickets * price)


# Task 1: the club gate has two bugs. Test it with age 20 and "yes" - should that person get in?
def fix_the_gate():
    age = int(input("Age: "))
    permission = input("Permission (yes/no): ")
    if age >= 13 or age <= 15:
        if permission == yes:
            print("Access granted")


# Task 2: write entry_check() - ages 13 to 15 with permission get in.
# It prints exactly one of: Access granted / Age out of range / Permission required


# Task 3: write score_level() - first check that the score is between 0 and 100, then print its level.


ticket_price()
# fix_the_gate()
# entry_check()
# score_level()
