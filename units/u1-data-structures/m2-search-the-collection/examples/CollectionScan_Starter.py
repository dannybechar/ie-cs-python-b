# Grade 9 - Unit 1 Meeting 2
# Read and predict before running.

values = [12, 7, 18, 4, 15]
target = 18
found = False
count_high = 0
total = 0
highest = values[0]

for value in values:
    total += value
    if value == target:
        found = True
    if value >= 10:
        count_high += 1
    if value > highest:
        highest = value

print(found, count_high, total, highest)
