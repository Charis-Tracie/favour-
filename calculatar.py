# Simple Python Calculator with 5 operations and helpful comments

def add(a, b):
    # Returns the sum of a and b
    return a + b

def subtract(a, b):
    # Returns the result of a minus b
    return a - b

def multiply(a, b):
    # Returns the product of a and b
    return a * b

def divide(a, b):
    # Checks for division by zero
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def difference(a, b):
    # Returns the absolute difference between a and b
    return abs(a - b)

def display_menu():
    # Shows available operations
    print("\n--- Simple Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Difference (|a - b|)")
    print("6. Exit")

def get_number(prompt):
    # Asks the user to input a number and handles invalid inputs
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    # Main loop of the calculator
    while True:
        display_menu()
        choice = input("Enter choice (1-6): ")

        # Exit condition
        if choice == '6':
            print("Goodbye!")
            break

        # Validate choice
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please select a number from 1 to 6.")
            continue

        # Get numbers from user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        # Perform selected operation
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = difference(num1, num2)

        # Display the result
        print("Result:", result)

# Run the calculator when the script is executed
if __name__ == "__main__":
    calculator()
