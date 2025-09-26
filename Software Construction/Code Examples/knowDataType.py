#type() function.
#The type() function returns the exact type of an object.
x = 10 
print(type(x)) # Output: <class 'int'> y = "hello" print(type(y)) # Output: <class 'str'> z = [1, 2, 3] print(type(z)) # Output: <class 'list'> isinstance() function.
#The isinstance() function is used to check if an object is an instance of a specified class or a subclass thereof. It is generally preferred over type() when checking for types, especially when dealing with inheritance, as it considers derived types.
x = 10 
print(isinstance(x, int)) # Output: True print(isinstance(x, float)) # Output: False
