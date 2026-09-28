# Warm-up: this is classical code - rules written by a person, not AI.
# Predict the output for 180 / yes, 180 / no and 100 / yes, then run and check.


def flag_message():
    message_length = int(input("Message length: "))
    has_link = input("Contains a link? (yes/no): ") == "yes"
    if message_length > 150 and has_link:
        print("Flag message")
    else:
        print("Allow message")


# Task 1: a rule for recognizing a kettle drawing. Try to break it:
# find a real kettle it misses, and something that is not a kettle that it accepts.
def kettle_rule():
    circles = int(input("Circles in the drawing: "))
    lines = int(input("Straight lines in the drawing: "))
    if circles == 1 and lines >= 2:
        print("kettle")
    else:
        print("not kettle")


flag_message()
# kettle_rule()
