# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty_list = []
# Accessing elements
print(numbers[0])    # First element: 1
print(numbers[-1])   # Last element: 5
print(fruits[1])     # Second element: "banana"
# Modifying lists
numbers.append(6)        # Add to end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)     # Insert at index: [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)        # Remove value: [0, 1, 2, 4, 5, 6]
popped = numbers.pop()   # Remove and return last element: 6


# List operations
numbers = [1, 2, 3, 4, 5]
# Slicing
print(numbers[1:3])   # [2, 3] - elements from index 1 to 2
print(numbers[:3])    # [1, 2, 3] - first three elements
print(numbers[2:])    # [3, 4, 5] - from index 2 to end
# List comprehension (powerful feature)
squares = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]
even_numbers = [x for x in numbers if x % 2 == 0]  # [2, 4]
# Iterating through lists
for number in numbers:
    print(number)
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

