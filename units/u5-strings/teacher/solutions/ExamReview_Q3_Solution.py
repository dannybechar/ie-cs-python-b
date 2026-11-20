# Question 3 solution: lower() first so Python and python both count
sentence = "Python is fun and Python is easy"
print("Python appears:", sentence.lower().count("python"))
changed = sentence.replace("easy", "great")
print("Changed:", changed)
print("New length:", len(changed))
