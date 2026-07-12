name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")

age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    print("You are " + str(age) + " years old.")
    

val = int(input("Enter a number: "))
print("The square of " + str(val) + " is " + str(val ** 2) + ".")