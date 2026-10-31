# Warm-up: this should count one step. Run it, read the error, and add one line to fix it.

counter = 0


def do_step():
    counter = counter + 1
    print("Step done!")


do_step()
print("Counter:", counter)


# Task 1 (paper, then run): local or global? See the lab brief for show_greeting and update_score.
app_name = "Math Quiz"


def show_greeting(user_name):
    welcome_msg = "Hello " + user_name
    print(welcome_msg)
    print("Welcome to " + app_name)


score = 50


def update_score():
    score = 100
    print("Inside function:", score)


# show_greeting("Dana")
# update_score()
# print("Outside function:", score)
# print(welcome_msg)                 # predict first: what happens?


# Task 2: define a global total_points = 0 and a function add_bonus(bonus) that adds bonus to it.
# Call add_bonus(10) twice and print total_points.


# Task 3 (variable roles): the two parking lots.
# parking_a() returns 20. parking_b(hours): up to 3 hours 5, up to 4 hours 15, more than that 30.
# compare_parking(hours) returns "Parking A is cheaper", "Parking B is cheaper" or "Same price".
# In the main program: print the answer for 2, 4, 10 and 24 hours.


# Task 4: write how_many_legs(animal) - spider 8, ant 6, dog or cat 4, chicken 2, anything else -1.
# Test it with input("Enter name of an animal: ").


# Checkpoint: donation campaign.
# Two global variables: sum_of_donations (starts at 0) and number_of_high_donors (starts at 0).
# Write add_donation(donation): add it to the sum; if it is more than 100, count one more high donor
# and print "Thank you, the certificate is on the way".
# Main program: read the number of donors, then read a donation for each donor and call add_donation.
# At the end print the two global variables.


# If time: add_coins(new_coins) with a global coins; weight_of_number(number) for a two-digit number
# (the product of its digits); split the "calculator" into four small functions that each return one value.
