results = [("Dana", 3), ("Ali", 5), ("Maya", 4), ("Noa", 2)]

print("Second name:", results[1][0])
print("Third score:", results[2][1])

results.append(("Omar", 6))
results[0] = ("Dana", 4)

for record in results:
    print(record[0], record[1])
