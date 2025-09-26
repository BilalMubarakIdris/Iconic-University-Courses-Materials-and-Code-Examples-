# Converting between data types
# String to number
num_str = "123"
num_int = int(num_str)    # 123
num_float = float(num_str) # 123.0
# Number to string
num = 456
num_as_str = str(num)     # "456"
# List to string
fruits = ["apple", "banana", "cherry"]
fruits_str = ", ".join(fruits)  # "apple, banana, cherry"
# String to list
text = "hello world"
words = text.split()      # ["hello", "world"]
# List to dictionary (for specific patterns)
pairs = [("a", 1), ("b", 2), ("c", 3)]
pairs_dict = dict(pairs)  # {"a": 1, "b": 2, "c": 3}
