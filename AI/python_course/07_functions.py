# Functions

def greet(name="friend"):
    return f"Hello, {name}!"

def area_of_circle(r):
    return 3.1416 * r * r

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)   # recursion

def stats(*nums):
    return min(nums), max(nums), sum(nums) / len(nums)

print(greet())
print(greet("Nymur"))
print("Area (r=3):", round(area_of_circle(3), 2))
print("5! =", factorial(5))
lo, hi, avg = stats(4, 8, 15, 16, 23, 42)
print("min:", lo, "max:", hi, "avg:", avg)

square = lambda x: x ** 2
print("Lambda square of 9:", square(9))
print("Even numbers:", list(filter(lambda x: x % 2 == 0, range(10))))
