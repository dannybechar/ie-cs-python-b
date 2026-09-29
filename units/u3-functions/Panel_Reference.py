# Unit 3.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: the call runs before Python has seen the def, so the name show_status
# is not defined yet. Move the def above the call.
def show_status():
    print("READY")


show_status()


# Task 1: the same two lines, reused with something in between
def show_welcome():
    print("WELCOME")
    print("Choose a mission")


def task1():
    show_welcome()
    print("---")
    show_welcome()


# Task 2 (mini-project): four short functions, one job each
def show_title():
    print("MISSION PANEL")


def show_help():
    print("Press ENTER to continue")


def show_end():
    print("Session complete")


def control_panel():
    show_title()
    show_status()
    show_help()
    show_status()
    show_end()


# task1()
control_panel()
