# Function to check if number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("Enter number: "))
print(f"The number is {check_even_odd(num)}")