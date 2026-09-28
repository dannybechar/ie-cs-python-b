# Unit 2.1 - reference for the teacher.
# One function per task. Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: every result comes from one rule a person wrote.
# 180 / yes -> Flag message; 180 / no -> Allow message; 100 / yes -> Allow message.
# Changing 150 to 100 changes the behavior - but the program is still rules, not AI.
def flag_message():
    message_length = int(input("Message length: "))
    has_link = input("Contains a link? (yes/no): ") == "yes"
    if message_length > 100 and has_link:
        print("Flag message")
    else:
        print("Allow message")


# Task 1: the rule is too narrow and too wide at the same time.
# Missed kettle: a tall electric kettle - 0 circles, 6 lines -> not kettle.
# False kettle: a road sign on a pole - 1 circle, 2 lines -> kettle.
# More conditions fix one drawing and break another: people draw in endless ways.
def kettle_rule():
    circles = int(input("Circles in the drawing: "))
    lines = int(input("Straight lines in the drawing: "))
    if circles == 1 and lines >= 2:
        print("kettle")
    else:
        print("not kettle")


# flag_message()
kettle_rule()
