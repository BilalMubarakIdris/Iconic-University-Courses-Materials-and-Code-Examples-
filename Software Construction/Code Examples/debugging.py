# Example of debugging a function
def calculate_discount(price, discount_percent):
    # Debug: Check input types
    print(f"Debug: price={price}, type={type(price)}")
    print(f"Debug: discount_percent={discount_percent}, type={type(discount_percent)}")
    
    # Convert to appropriate types if needed
    try:
        price = float(price)
        discount_percent = float(discount_percent)
    except ValueError:
        print("Error: Both inputs must be numeric")
        return None
    # Check for valid values
    if price < 0:
        print("Error: Price cannot be negative")
        return None
    if discount_percent < 0 or discount_percent > 100:
        print("Error: Discount must be between 0 and 100")
        return None
    # Calculate discount
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    print(f"Debug: discount_amount={discount_amount}, final_price={final_price}")
    return final_price
# Test the function
result = calculate_discount(100, 20)  # Should return 80
print(f"Result: {result}")
