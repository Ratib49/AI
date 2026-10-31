# Modules and exception handling

import math
import random
from datetime import date

print("sqrt(144) =", math.sqrt(144))
print("pi =", round(math.pi, 4))
random.seed(1)
print("Random dice roll:", random.randint(1, 6))
print("Today:", date.today())

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Cannot divide {a} by zero")
        return None
    else:
        return result
    finally:
        print("Division attempted")

print(safe_divide(10, 2))
print(safe_divide(10, 0))

try:
    int("abc")
except ValueError as e:
    print("ValueError caught:", e)
