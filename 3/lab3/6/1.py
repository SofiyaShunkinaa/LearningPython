some_values = [1, "A", 8, 0, "+", "Y", "B", ".", "K", 8]

numbers = set()
letters = set()
for value in some_values:
    value = str(value)
    for char in value:
        char = str(char)
        if 32 <= ord(char) <= 64:
            numbers.add(char)
        if 65 <= ord(char) <= 70 or 88 <= ord(char) <= 90:
            letters.add(char)
print(numbers)
print(letters)
