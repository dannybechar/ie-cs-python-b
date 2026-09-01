stock = {"pencil": 12, "eraser": 5, "notebook": 8, "marker": 4}

item = input("Item: ")
if item in stock:
    stock[item] = stock[item] - 1
    print("Remaining:", stock[item])
else:
    print("Item not found")

stock["folder"] = 6
stock["eraser"] = 9
print("Items tracked:", len(stock))
