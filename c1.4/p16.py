student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "email": "john.doe@example.com",
    "subjects": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    1 : "one",
    12.99 : "twelve point nine nine"
}

# Dictionaries are used to store data in key-value pairs. Each key is unique and is used to access the corresponding value.
# Dictionaries are mutable, meaning you can change their contents after creation.
# Dictionaries can be nested, meaning you can have dictionaries within dictionaries.
# Dictionaries can be used to represent real-world entities, such as a student, with various attributes.

print(student["name"])  # Output: John Doe
print(student["age"])   # Output: 20
print(student["grade"]) # Output: A
print(student["email"]) 

print(student["subjects"])  # Output: ['Math', 'Science', 'History']
print(student["address"]["city"])  # Output: Anytown

print(student[1])  # Output: one
print(student[12.99])  # Output: twelve point nine nine

# Dictionary Methods

print(student.keys())    # Output: dict_keys(['name', 'age', 'grade', 'email', 'subjects', 'address', 1, 12.99])
print(student.values())  # Output: dict_values(['John Doe', 20, 'A
print(student.items())   # Output: dict_items([('name', 'John Doe'), ('age', 20), ('grade', 'A'), ('email', '
print(student.get("name"))  # Output: John Doe
#print(student.get("phone"))  # Output: None
#print(student["phone"])  # Output: KeyError: 'phone'
# .get() method is used to access the value of a key in a dictionary. If the key does not exist, it returns None or a default value if provided.
print(student.get("phone", "Not Found"))  # Output: Not Found
print(len(student))  # Output: 8

new_dict = { "parentName": "John Doe A" }

student.update(new_dict)  # Updates the student dictionary with new_dict
print(student)  