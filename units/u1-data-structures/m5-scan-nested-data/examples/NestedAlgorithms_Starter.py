# Grade 9 - Unit 1 Meeting 5
# Read and predict before running.

records = [("Dana", 82), ("Ali", 91), ("Maya", 76), ("Omar", 88)]

total = 0
count_high = 0
top_name = records[0][0]
top_score = records[0][1]

for record in records:
    score = record[1]
    total += score
    if score >= 80:
        count_high += 1
    if score > top_score:
        top_name = record[0]
        top_score = score

print(total, count_high, top_name, top_score)
