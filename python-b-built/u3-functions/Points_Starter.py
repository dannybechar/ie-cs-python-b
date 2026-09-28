# Warm-up: predict what will print, run it, then add one word to fix it.


def discounted(price, percent):
    discount = price * percent / 100
    price - discount


final_price = discounted(80, 25)
print(final_price)


# Task 1: write is_even(number) - returns True or False. No print inside the function.
# Test it with 14 and with 9.


# Task 2: write passed(score) - returns True if score >= 60. Use it inside an if/else
# that prints "Continue" or "Try again".


# Task 3 (checkpoint): a task calculator, three small functions:
# calculate_points(level, tasks) -> level * tasks * 10
# passed_checkpoint(points) -> True if points >= 100
# show_result(name, points, success) -> prints name, points, success
# Build and test each one alone first, then call all three from one flow.
