# Using booleans to control program flow
def check_access(user_age, has_subscription):
    # Check if user is adult
    is_adult = user_age >= 18
    # Check if content can be accessed
    if is_adult and has_subscription:
        return "Full access granted"
    elif is_adult and not has_subscription:
        return "Please subscribe for full access"
    else:
        return "Access denied - age restriction"
# Test the function
print(check_access(25, True))   # Full access granted
print(check_access(25, False))  # Please subscribe for full access
print(check_access(16, True))   # Access denied - age restriction
