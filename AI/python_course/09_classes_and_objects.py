# Classes and objects (basic OOP)

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def __str__(self):
        return f"{self.name} (Roll {self.roll}) - avg {self.average():.2f}"


class GraduateStudent(Student):      # inheritance
    def __init__(self, name, roll, thesis):
        super().__init__(name, roll)
        self.thesis = thesis

    def __str__(self):
        return super().__str__() + f", thesis: {self.thesis}"


s1 = Student("Rina", 1)
for m in (80, 75, 90):
    s1.add_mark(m)

s2 = GraduateStudent("Sajid", 2, "Graph search in AI")
s2.add_mark(88)

print(s1)
print(s2)
