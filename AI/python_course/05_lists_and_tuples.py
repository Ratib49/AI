# Lists and tuples

fruits = ["mango", "banana", "apple"]
fruits.append("jackfruit")
fruits.insert(1, "guava")
print("Fruits:", fruits)

fruits.remove("banana")
print("After remove:", fruits)
print("Popped:", fruits.pop())
print("Now:", fruits)

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted:", numbers)
print("Max:", max(numbers), "Min:", min(numbers), "Sum:", sum(numbers))

squares = [x * x for x in range(1, 6)]
print("Squares (list comprehension):", squares)

point = (3, 4)          # tuple is immutable
x, y = point
print("Tuple:", point, "x =", x, "y =", y)

matrix = [[1, 2, 3], [4, 5, 6]]
for row in matrix:
    print(row)
