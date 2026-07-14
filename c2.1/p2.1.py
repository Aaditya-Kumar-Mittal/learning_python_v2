developer = 'Aaditya Kumar Mittal'
print(list(developer))

developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer)

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) 
print(rest)

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4])

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers)

numbers.extend(even_numbers)
print(numbers)

numbers.insert(2, 2.5)

print(numbers)

numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers)

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers) # sorted() function returns a new sorted list without modifying the original list

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers)

developer = 'Jessica'
print(tuple(developer))

# If you need to remove an item from a tuple, that isn't possible because tuples are immutable.