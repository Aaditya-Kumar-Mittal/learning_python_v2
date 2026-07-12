# Type Conversion in Python

# Type conversion is the process of converting one data type to another data type in Python.
# There are two types of type conversion in Python:
# 1. Implicit Type Conversion (Type Conversion) -- Done by Python automatically by interpreter
# 2. Explicit Type Conversion (Type Casting) -- Done by the programmer

# Implicit Type Conversion (Type Conversion)
# In implicit type conversion, Python automatically converts one data type to another data type without any user
# intervention. This is done when we perform operations on different data types.

a = 10      # Integer
b = 20.5    # Float
sum = a + b  # Implicit type conversion from int to float
print("The sum of a and b is:", sum)

# Explicit Type Conversion (Type Casting)
# In explicit type conversion, the programmer converts one data type to another data type using built-in
# functions like int(), float(), str(), etc.
c = "20"  # String
d = 30    # Integer
sum = float(c) + d  # Explicit type conversion from string to float
print("The sum of c and d is:", sum)
