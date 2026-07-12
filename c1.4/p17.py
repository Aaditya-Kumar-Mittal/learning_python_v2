numSet = {1, 2, 3, 4, 5, 2, 3, 4, 5 , 'hello', 'world', 'hello', 'world'}  # Sets are unordered collections of unique elements. Duplicates are automatically removed.
print(numSet)  

print(type(numSet))  # Output: <class 'set'>

print(len(numSet))  # Output: 5 

emptySet = {} # This creates an empty dictionary, not a set. To create an empty set, use set().

print(type(emptySet))  # Output: <class 'dict'>

emptySet = set()  # This creates an empty set.
print(type(emptySet))  # Output: <class 'set'>

numSet.add(6)  # Adds an element to the set

print(numSet)  # Output: {1, 2, 3, 4, 5, 'hello', 'world', 6}

numSet.remove(3)  # Removes an element from the set. Raises KeyError if the element is not found.
print(numSet)  # Output: {1, 2, 4, 5, 'hello', 'world', 6}

numSet.discard(10)  # Removes an element from the set if it exists. Does not raise an error if the element is not found.
print(numSet)  # Output: {1, 2, 4, 5, 'hello', 'world', 6}

numSet.clear()  # Removes all elements from the set
print(numSet)  # Output: set()

numSet = {1, 2, 3, 4, 5}
print(numSet)  # Output: {1, 2, 3, 4, 5}

numSet.update({6, 7, 8})  # Adds multiple elements to the set
print(numSet)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

numSet.update([9, 10])  # Adds multiple elements from a list to the set
print(numSet)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}   

numSet.pop()  # Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
print(numSet)  # Output: (the output may vary since sets are unordered)


ASet = {1, 2, 3, 4, 5}
BSet = {4, 5, 6, 7, 8}
print(ASet.union(BSet))  # Output: {1, 2, 3, 4, 5, 6, 7, 8} - Returns a new set with all elements from both sets
print(ASet.intersection(BSet))  # Output: {4, 5} - Returns a new set with elements common to both sets
print(ASet.difference(BSet))  # Output: {1, 2, 3} - Returns a new set with elements in ASet but not in BSet
print(ASet.symmetric_difference(BSet))  # Output: {1, 2, 3, 6, 7, 8} - Returns a new set with elements in either ASet or BSet but not in both
print(BSet.issubset(ASet))  # Output: False - Returns True if BSet is a subset of ASet
print(ASet.issuperset(BSet))  # Output: False - Returns True if ASet is a superset of BSet
print(ASet.isdisjoint(BSet))  # Output: False - Returns True if ASet and BSet have no elements in common
print(BSet.difference(ASet))  # Output: {6, 7, 8} - Removes all elements of ASet from BSet

CSet = {9, 9.0}

print(CSet)  # Output: {9} - Demonstrates that 9 and 9.0 are considered the same element in a set

CSet = {9, '9.0'}
print(CSet)  # Output: {9, '9.0'} - Demonstrates that 9 and '9.0' are considered different elements in a set

CSet = {('int', 9), ('float', 9.0)}

print(CSet)  # Output: {('int', 9), ('float', 9.0)} - Demonstrates that tuples can be elements of a set, but they must be hashable and unique