# for loop, while loop, break, continue

print("Numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("\nMultiplication table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print("\nSum of 1 to 100 =", total)

print("\nSkip 3, stop at 7:")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end=" ")
print()

print("\nStar pattern:")
for i in range(1, 5):
    print("*" * i)
