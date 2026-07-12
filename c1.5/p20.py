num = int(input("Enter a number: "))

print(f"Printing Table of {num}")

# range(1, 11) generates numbers from 1 to 10 (inclusive of 1 and exclusive of 11)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")