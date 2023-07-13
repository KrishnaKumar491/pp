# Write a Python program to find the factorial of a given number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
