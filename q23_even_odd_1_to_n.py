# Function and loop to print numbers 1 to n with even/odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(f"{i} -> {check_even_odd(i)}")