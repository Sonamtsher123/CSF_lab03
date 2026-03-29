# Print numbers 1 to 10 but skip 5 using continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()