marks = [50,60,70,80,90]

print(marks)

print(type(marks))

for mark in marks:
    print(mark)
    
for i in range(len(marks)):
    print(f"Mark at index {i} is {marks[i]}")

student1 = ["John", 20, "Male", 122101]
student2 = ["Johnny", 20, "Male", 122102]
print(student1)
print(student2)

# Strings are immutable, but lists are mutable.

student1[0] = "John Doe"
print(student1)

# List Slicing

charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(charList[0:4])  # prints elements from index 0 to 3
print(charList[0:])  # prints elements from index 0 to the end of the list
print(charList[:]) 
print(charList[-1]) 
print(charList[-4:-1]) 
print(charList[:len(charList)])  # prints all elements of the list
print(charList[::2])  # prints every second element of the list
print(charList[3::4])  # prints every second element of the list

