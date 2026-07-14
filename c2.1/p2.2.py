
# The range() function is used to generate a sequence of integers. - range(start, stop, step)
# The required stop argument is an integer that represents the end point for the sequence of numbers being generated. 

for num in range(3):
    print(num)
    
for num in range(1, 5):
    print(num)
    
for num in range(40, 0, -10):
    print(num)
    
numbers = list(range(2, 11, 2))
print(numbers)

languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
    
# The enumerate() function also accepts an optional start argument that specifies the starting value for the count. If this argument is omitted, then the count will begin at 0. 

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')
    

# You can use the zip() function for that, which combines lists into pairs of elements and returns an iterator of tuples.
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')