from datetime import datetime

def timestamp_decorator(func):
    def wrapper(*args, **kwargs):
        # Print the timestamp before the function execution
        print(f"Timestamp before execution: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Call the original function
        result = func(*args, **kwargs)

        # Print the timestamp after the function execution
        print(f"Timestamp after execution: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        return result

    return wrapper

# Apply the decorator to ordinary functions

@timestamp_decorator
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    return result

@timestamp_decorator
def multiply_numbers(a, b):
    result = a * b
    print(f"The product of {a} and {b} is {result}")
    return result

# Test the decorated functions
add_numbers(3, 4)
multiply_numbers(2, 5)
