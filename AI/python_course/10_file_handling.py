# File handling: write, append, read, and CSV

import csv
import os

folder = os.path.dirname(os.path.abspath(__file__))
txt_file = os.path.join(folder, "notes.txt")
csv_file = os.path.join(folder, "students.csv")

# write (creates or overwrites)
with open(txt_file, "w", encoding="utf-8") as f:
    f.write("Line 1: Python file handling\n")
    f.write("Line 2: Writing to a file\n")

# append
with open(txt_file, "a", encoding="utf-8") as f:
    f.write("Line 3: This line was appended\n")

# read whole file
with open(txt_file, "r", encoding="utf-8") as f:
    print("Full file:\n" + f.read())

# read line by line
with open(txt_file, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(i, "->", line.strip())

# CSV write and read
rows = [["name", "marks"], ["Rina", 85], ["Sajid", 78], ["Tania", 92]]
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} got {row['marks']}")

print("\nFile exists?", os.path.exists(txt_file))
