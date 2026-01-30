# Simple calculator module 

def python_calculator(x, y):

    print("Select operation.")
    print("+. Addition.")
    print("-. Subtraction.")
    print("*. Multiplication.")
    print("/. Division.")
   
    choice = input("\nEnter operation: ")
    # Take input for calculation
    x = int(input(": "))
    y = int(input(": "))
   
    # Addition
    if choice == "+":
        result = x + y
        print(f"\n{x} + {y} = {result}")

    # Subtraction
    elif choice == "-":
        result = x - y
        print(f"\n{x} - {y} = {result}")

    # Multiplication
    elif choice == "*":
        result = x * y
        print(f"\n{x} * {y} = {result}")

    # Division
    elif choice == "/":
        result = x / y
        print(f"\n{x} / {y} = {result}")

    # Syntax Error
    else:
        print("Syntax Error")

if __name__ == "__main__":
    python_calculator(0, 0)
