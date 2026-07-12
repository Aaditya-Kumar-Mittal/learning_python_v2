tup1 = ("C", "D", "A", "A", "B", "C", "D", "B", "C", "D", "A")

print(f"Count of 'A' in the tuple: {tup1.count('A')}")

print(f"Length of the tuple: {len(tup1)}")

emptyList = []

for i in range(len(tup1)):
    emptyList.append(tup1[i])
    
print(f"List created from the tuple: {emptyList}")