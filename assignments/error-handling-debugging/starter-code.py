# Error Handling & Debugging - Starter Code
# Complete the tasks below to learn about error handling and debugging in Python

# ============================================================================
# TASK 1: Fix the Errors
# ============================================================================
# The following code has intentional errors. Read the error messages,
# identify the bugs, and fix them.

def task_1_fix_errors():
    print("=== TASK 1: Fix the Errors ===\n")
    
    # Bug 1: What happens when you divide by zero?
    result1 = 10 / 0
    print(f"10 divided by 0 is: {result1}")
    
    # Bug 2: String cannot be added to an integer
    result2 = "Hello" + 5
    print(f"String concatenation: {result2}")
    
    # Bug 3: Index out of range
    my_list = [1, 2, 3]
    result3 = my_list[5]
    print(f"List element at index 5: {result3}")
    
    # Bug 4: Attribute doesn't exist
    name = "Alice"
    result4 = name.append("!")
    print(f"Modified name: {result4}")


# ============================================================================
# TASK 2: Handle Exceptions
# ============================================================================
# Complete the function below. Use try/except blocks to catch exceptions
# and handle them gracefully.

def task_2_handle_exceptions():
    print("\n=== TASK 2: Handle Exceptions ===\n")
    
    # TODO: Wrap this code in try/except blocks to catch exceptions
    # Try catching ValueError, ZeroDivisionError, and IndexError
    
    user_input = input("Enter a number: ")
    number = int(user_input)  # Can raise ValueError
    
    result = 100 / number  # Can raise ZeroDivisionError
    print(f"100 divided by {number} is: {result}")
    
    my_list = [10, 20, 30]
    index = int(input("Enter a list index: "))
    print(f"Item at index {index}: {my_list[index]}")  # Can raise IndexError
    
    print("All operations completed successfully!")


# ============================================================================
# TASK 3: Build a Robust Input Validator
# ============================================================================
# Complete the functions below to validate user input

def validate_age(age_input):
    """
    TODO: Validate that age is a number and between 0 and 150.
    Raise ValueError with a descriptive message if invalid.
    """
    pass


def validate_email(email_input):
    """
    TODO: Validate that email contains an '@' symbol.
    Raise ValueError with a descriptive message if invalid.
    """
    pass


def task_3_robust_validator():
    print("\n=== TASK 3: Robust Input Validator ===\n")
    
    validated_data = {}
    
    # TODO: Use try/except to collect valid age
    # Keep asking until valid input is received
    
    # TODO: Use try/except to collect valid email
    # Keep asking until valid input is received
    
    # Display the validated data
    print("\n✓ Thank you! Here's your information:")
    print(f"Age: {validated_data.get('age')}")
    print(f"Email: {validated_data.get('email')}")


# ============================================================================
# Main Program
# ============================================================================

if __name__ == "__main__":
    try:
        task_1_fix_errors()
    except Exception as e:
        print(f"Error in Task 1: {e}")
    
    try:
        task_2_handle_exceptions()
    except Exception as e:
        print(f"Error in Task 2: {e}")
    
    try:
        task_3_robust_validator()
    except Exception as e:
        print(f"Error in Task 3: {e}")
