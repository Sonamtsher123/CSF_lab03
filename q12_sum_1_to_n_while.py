# Sum from 1 to n using while loop
n = int(input("Enter n: "))
sum_nums = 0
i = 1

while i <= n:
    sum_nums += i
    i += 1

print(f"Sum = {sum_nums}")