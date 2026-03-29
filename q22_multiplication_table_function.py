# Function to print multiplication table
def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Enter number: "))
print_table(num)