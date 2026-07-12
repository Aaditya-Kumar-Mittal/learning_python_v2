# Sum of n natural numbers using recursion
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)

# Example usage
n = 5
print(f"The sum of first {n} natural numbers is: {sum_natural(n)}")