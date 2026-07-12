'''
def sum(num1, num2):
    return num1 + num2

print(sum(5, 10))
print(sum(5, 15))
'''

def sum(num1, num2):
    return num1 + num2

a = 10
b = 20
c = 30

avg = sum(sum(a, b), c) // 3
print(f"The average of {a}, {b}, and {c} is: {avg}")