sqTuple = ()

n = 10

for i in range(1, n + 1):
    sqTuple += (i ** 2,)

print(sqTuple)


num = int(input("Enter a number to search in tuple: "))

if num in sqTuple:
    print(f"{num} is present in the tuple.")
else:
    print(f"{num} is not present in the tuple.")