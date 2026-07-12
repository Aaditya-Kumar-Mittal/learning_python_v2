print("I am Aaditya Kumar Mittal!")
print("I am Aaditya Kumar Mittal!", "I am Aaditya Kumar Mittal!")

name = "Aaditya Kumar Mittal"
age = 20
price = 23.5

# print is a function that outputs text to the console. It can take multiple arguments and will print them separated by spaces. In this case, we are using an f-string to format the output with variables.
print(f"Hello, my name is {name} and I am {age} years old.")

print(type(name))  # This will print <class 'str'> because name is a string
print(type(age))   # This will print <class 'int'> because age is an integer
print(type(price)) # This will print <class 'float'> because price is a float

name1 = "Aaditya Kumar Mittal"
name2 = 'Aaditya Kumar Mittal'
name3 = """Aaditya Kumar Mittal"""
name4 = '''Aaditya Kumar Mittal'''

print(type(name1))  # This will print <class 'str'> because name1 is a string
print(type(name2))  # This will print <class 'str'> because name2 is a string
print(type(name3))  # This will print <class 'str'> because name3 is a string
print(type(name4))  # This will print <class 'str'> because name4 is a string

a = None
b = False
c = True
print(type(a))  # This will print <class 'NoneType'> because none is None
print(type(b))  # This will print <class 'bool'> because false is a boolean
print(type(c))   # This will print <class 'bool'> because true is a boolean