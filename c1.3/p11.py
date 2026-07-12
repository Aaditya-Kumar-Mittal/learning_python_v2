numList = [5,1,6,8,3,6]

print("Original List:", numList)

numList.append(10)

print("List after appending 10:", numList)

numList.sort()

print("Sorted List:", numList)

numList.sort(reverse=True)

print("Sorted List in Descending Order:", numList)

numList.reverse()

print("Reversed List:", numList)

numList.insert(2, 15)

print("List after inserting 15 at index 2:", numList)

numList.remove(6)

print("List after removing 6:", numList)

numList.pop(0)

print("List after popping the first element:", numList)

numList.pop()

print("List after popping the last element:", numList)

numList.clear()

print("List after clearing all elements:", numList)