name = "Aaditya Kumar Mittal"

for i in range(len(name)):
    print(f"Character at index {i} is {name[i]}")

# Slicing in Python

firstName = name[0:7]
print(f"First name is {firstName}")

middleName = name[8:13]
print(f"Middle name is {middleName}")

lastName = name[14:20]
print(f"Last name is {lastName}")

firstName2 = name[:7]
print(f"First name is {firstName2}")

lastName2 = name[14:]
print(f"Last name is {lastName2}")

lastName3 = name[-6:]
print(f"Last name is {lastName3}")

firstName3 = name[:-13]
print(f"First name is {firstName3}")

middleName2 = name[8:-6]
print(f"Middle name is {middleName2}")

middleName3 = name[-12:-6]
print(f"Middle name is {middleName3}")