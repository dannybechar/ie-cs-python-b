# Warm-up: the total is wrong. Predict the output for 1, 2, 3, 4, 5, run it, then fix one line.


def sum_five():
    total = 0
    for day in range(1, 6):
        score = int(input("Score: "))
        total = score
    print("Total:", total)


# Task 1: write countdown() - 10, 9, ... 1 and then Go!
# and evens() - 2, 4, 6 ... 20. One for loop each.


# Task 2: fill in the trace table in the brief BEFORE you run this. Inputs: 80, 70, 100
def trace_me():
    total = 0
    high = 0
    for i in range(3):
        score = int(input("Score: "))
        total = total + score
        if score >= 80:
            high = high + 1
    print("Total:", total, "High:", high)


# Task 3: write five_scores() - the average of five scores and how many are 80 or more.


sum_five()
# countdown()
# evens()
# trace_me()
# five_scores()
