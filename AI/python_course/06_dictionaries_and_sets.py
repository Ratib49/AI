# Dictionaries and sets

student = {"name": "Karim", "id": 101, "cgpa": 3.65}
student["dept"] = "CSE"
print("Student:", student)
print("Name:", student["name"])
print("Phone:", student.get("phone", "not given"))

for key, value in student.items():
    print(f"  {key}: {value}")

# counting words with a dictionary
sentence = "ai is fun and ai is the future"
count = {}
for w in sentence.split():
    count[w] = count.get(w, 0) + 1
print("Word count:", count)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Remove duplicates:", set([1, 1, 2, 2, 3]))
