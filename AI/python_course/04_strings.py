# Working with strings

text = "Artificial Intelligence"
print("Original:", text)
print("Length:", len(text))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("First letter:", text[0])
print("Last letter:", text[-1])
print("Slice [0:10]:", text[0:10])
print("Reversed:", text[::-1])
print("Replace:", text.replace("Intelligence", "Life"))
print("Words:", text.split())
print("Count of 'i':", text.lower().count("i"))

word = "madam"
print(word, "is palindrome?", word == word[::-1])

name, score = "Rahim", 92.5
print(f"{name} scored {score:.1f}%")
