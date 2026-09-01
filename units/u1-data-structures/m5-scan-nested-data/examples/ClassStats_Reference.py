records = [("Dana", 82), ("Ali", 91), ("Maya", 76), ("Omar", 88)]

total = 0
count_high = 0
top_name = records[0][0]
top_score = records[0][1]
selected = []

for record in records:
    name = record[0]
    score = record[1]
    total += score
    if score >= 80:
        count_high += 1
    if score > top_score:
        top_name = name
        top_score = score
    if score >= 85:
        selected.append(name)

print("Total:", total)
print("At least 80:", count_high)
print("Top:", top_name, top_score)
print("Selected count:", len(selected))
