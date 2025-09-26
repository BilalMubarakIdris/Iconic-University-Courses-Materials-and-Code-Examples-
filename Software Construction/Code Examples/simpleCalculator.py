num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
        result = None
else:
    print("Error: Invalid operator")
    result = None

if result is not None:
    print(f"Result: {result}")
