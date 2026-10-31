# Operators and if / elif / else

a, b = 17, 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** 2 =", a ** 2)

print("a > b:", a > b)
print("a == b:", a == b)
print("a > 10 and b < 10:", a > 10 and b < 10)

marks = 78
if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 33:
    grade = "Pass"
else:
    grade = "Fail"
print(f"Marks {marks} -> Grade {grade}")

number = 14
print(number, "is", "even" if number % 2 == 0 else "odd")
