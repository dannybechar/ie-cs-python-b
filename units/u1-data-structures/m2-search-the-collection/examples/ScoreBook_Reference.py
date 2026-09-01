scores = {"Dana": 82, "Ali": 91, "Maya": 76}

name = input("Student name: ")
if name in scores:
    print("Score:", scores[name])
else:
    print("Student not found")

scores["Maya"] = 80
scores["Omar"] = 88
del scores["Dana"]

print("Students in book:", len(scores))
