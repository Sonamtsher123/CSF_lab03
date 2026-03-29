# Menu-driven calculator using functions and loop until exit
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 5:
        print("Exiting calculator...")
        break
    
    if choice in [1, 2, 3, 4]:
        a = float(input("Enter two numbers: "))
        b = float(input())
        
        if choice == 1:
            print(f"Sum = {add(a, b)}")
        elif choice == 2:
            print(f"Difference = {subtract(a, b)}")
        elif choice == 3:
            print(f"Product = {multiply(a, b)}")
        elif choice == 4:
            print(f"Quotient = {divide(a, b)}")
    else:
        print("Invalid choice. Please try again.")