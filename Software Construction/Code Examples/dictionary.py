# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}
empty_dict = {}
# Accessing values
print(student["name"])      # "Alice"
print(capitals["France"])   # "Paris"
# Using get() method to avoid KeyError
print(student.get("height", "Not available"))  # "Not available"



# # Dictionary operations
# student = {"name": "Alice", "age": 20, "major": "CS"}

# # Adding/updating elements
# student["gpa"] = 3.8 # Add new key-value pair
# student["age"] = 21  # Update existing value

# # Removing elements
# removed_value = student.pop("major") # Remove and return value
# del student["age"]   # Remove key-value pair


# # Iterating through dictionaries
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}: {value}")

# # Dictionary methods
# print(student.keys())     # List of keys
# print(student.values())   # List of values
# print(student.items())    # List of key-value tuples
