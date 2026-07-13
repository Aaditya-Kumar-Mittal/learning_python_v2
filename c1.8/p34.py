class Student:
    
    subjects = ["Math", "Science", "History"]  # Class variable shared by all instances
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self)
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Alice", 20)
s1.display()  
print(s1.subjects)
print(Student.subjects)