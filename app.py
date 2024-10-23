from calc_function import do_addition, do_substraction, do_division
from multiply import multi

def main():
    print("Welcome to the calculator")
    print("\n1. Addition\n2. Subtraction\n3. Multiplication")

    # Get user inputs
    user_input = input("Select the function (1, 2, or 3): ")
    print(f"User selected: {user_input}")  # Debugging statement to check input

    a = int(input("Enter the first number: "))  # Convert input to int
    print(f"First number entered: {a}")  # Debugging statement

    b = int(input("Enter the second number: "))  # Convert input to int
    print(f"Second number entered: {b}")  # Debugging statement

    # Check user choice and call appropriate function
    if user_input == "1":
        result = do_addition(a, b)
    elif user_input == "2":
        result = do_substraction(a, b)
    elif user_input == "3":
        result = multi(a, b)
        
    elif user_input =='4':
        result = do_division(a,b)
    else:
        print("Invalid input")
        return

    print(f"Result: {result}")  # Print the result

if __name__ == "__main__":
    main()
