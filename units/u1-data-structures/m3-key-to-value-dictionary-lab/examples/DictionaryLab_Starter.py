# Grade 9 - Unit 1 Meeting 3
# Read and predict before running.

stock = {"pencil": 12, "eraser": 5, "notebook": 8}

print(stock["pencil"])
stock["eraser"] = 7
stock["marker"] = 4

if "notebook" in stock:
    stock["notebook"] -= 1

print(len(stock))
print(stock["notebook"])
