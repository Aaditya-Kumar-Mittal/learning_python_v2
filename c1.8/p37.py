class Person:
    
    __name = "John Doe"  # Private class variable
    
    def __init__(self, age):
        self.age = age  # Public instance variable
    
    def __hello(self):  # Private method
        print(f"Hello, my name is {self.__name} and I am {self.age} years old.")

p1 = Person(30)
# Accessing the private method using name mangling
p1._Person__hello()  # Output: Hello, my name is John Doe and I am 30 years old.
