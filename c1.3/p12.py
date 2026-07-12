tup1 = (1,2,3,4,5,6,7,8,9,10)

# Tuples are immutable, but lists are mutable.

print(tup1)

print(type(tup1))

print(tup1[0])  # prints the first element of the tuple

print(len(tup1))  # prints the length of the tuple

print(tup1[0:4])  # prints elements from index 0 to 3

print(tup1[0:])  # prints elements from index 0 to the end of the tuple

print(tup1[:])  # prints all elements of the tuple

print(tup1[-1])  # prints the last element of the tuple

print(tup1[-4:-1])  # prints elements from index -4 to -2

print(tup1[:len(tup1)])  # prints all elements of the tuple

print(tup1[::2])  # prints every second element of the tuple

print(tup1[3::4])  # prints every fourth element of the tuple starting from index 3

print(tup1.count(5))  # prints the count of the element 5 in the tuple

print(tup1.index(5))  # prints the index of the first occurrence of the element 5 in the tuple