reads = [
    ("Dana", "Fantasy", 120),
    ("Ali", "Science", 80),
    ("Dana", "Mystery", 60),
    ("Maya", "Fantasy", 150),
    ("Ali", "Fantasy", 40)
]

total_pages = 0
large_entries = 0
unique_genres = set()
pages_by_student = {}

for record in reads:
    name = record[0]
    genre = record[1]
    pages = record[2]

    total_pages += pages
    if pages >= 100:
        large_entries += 1
    unique_genres.add(genre)

    if name in pages_by_student:
        pages_by_student[name] += pages
    else:
        pages_by_student[name] = pages

top_reader = None
top_pages = -1
for name in pages_by_student:
    if pages_by_student[name] > top_pages:
        top_reader = name
        top_pages = pages_by_student[name]

print("Total pages:", total_pages)
print("Entries >= 100:", large_entries)
print("Unique genres:", len(unique_genres))
print("Top reader:", top_reader, top_pages)
