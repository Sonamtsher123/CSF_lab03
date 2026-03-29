# Search for a number in a list and stop when found
numbers = [2, 4, 6, 8, 10]
print(f"List: {' '.join(map(str, numbers))}")

search = int(input("Searching for: "))

for num in numbers:
    if num == search:
        print("Number found")
        break