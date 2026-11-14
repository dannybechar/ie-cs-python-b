# Teacher helper (not for students): turns a Google Forms CSV export into three lines of Python
# (item_names, aliases, answers) that students paste into their files. Run it once on the class
# survey and copy the output. Header: alias, then one column per item. Every cell: V, X or 0.
# It uses open / readline / split, which the class has not learned - that is why it is a teacher tool.

filename = "ratings.csv"

file = open(filename, "r", encoding="utf-8-sig")
header = file.readline().strip().split(",")

items_text = ""
for name in header[1:]:
    if items_text != "":
        items_text += ", "
    items_text += "\"" + name.strip() + "\""

aliases_text = ""
answers_text = ""
for line in file:
    line = line.strip()
    if line == "":
        continue
    cells = line.split(",")
    row = ""
    for cell in cells[1:]:
        cell = cell.strip()
        if cell != "V" and cell != "X" and cell != "0":
            print("WARNING:", cells[0], "has a bad cell:", cell, "- fix it in the file")
        row += cell
    if aliases_text != "":
        aliases_text += ", "
        answers_text += ", "
    aliases_text += "\"" + cells[0].strip() + "\""
    answers_text += "\"" + row + "\""
file.close()

print("item_names = [" + items_text + "]")
print("aliases = [" + aliases_text + "]")
print("answers = [" + answers_text + "]")
