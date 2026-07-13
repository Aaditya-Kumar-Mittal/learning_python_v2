class Student:
    
    subjects = ["Math", "Science", "History"]  # Class variable shared by all instances
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @staticmethod # This decorator indicates that the method is a static method. Static methods work at class level and do not require an instance to be called. They can be called using the class name or an instance of the class.
    def sayGreetings():
        print("Hello, welcome to the class!")

    def display(self):
        print(self)
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Alice", 20)
s1.display()
s1.sayGreetings()  # Calling the static method using the instance
Student.sayGreetings()  # Calling the static method using the class name