# List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets. This makes the code shorter and often easier to read.

even_numbers = [num for num in range(0, 30) if num % 2  == 0]
print(even_numbers)

characters = ['a', 'b', 'c', 'd', 'e']

vowel_characters = [char for char in characters if char in 'aeiou']
print(vowel_characters)

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)

#he filter() function is used to select elements from an iterable that meet a specific condition. The filter() function accepts a function and an iterable for its arguments. In this example, we are passing in an is_long_word function into the filter() function to check if the current word count is greater than 4. All words that have a character count greater than 4 are added into a new list and assigned to the long_words variable.


celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)

numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) 


numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total)

numbers = [5, 10, 15, 20]
squares = list(map(lambda x: x**2, numbers))
print(squares)
