# Write a Python program to find the sum of all the numbers in a given list.
def sum_of_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

# Test the function
print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15
print(sum_of_list([-1, 0, 1]))        # Output: 0
