# Write a Python program to count the number of vowels in a given string.
def count_vowels(string):
    vowels = 'AEIOU'
    count = 0
    for char in string:
        if char.upper() in vowels:
            count += 1
    return count

# Test the function
print(count_vowels('ENVIRONMENT'))  
