# Sample list of tuples
data = [(1, 0.4), (2, 0.2), (3, 0.6), (4, 0.1), (5, 0.8)]
# Filter tuples based on conditions (value greater than 0.3 and limit to 5 elements)
filtered_data = list(filter(lambda x: x[1] > 0.3, data))[:5]
print(filtered_data)

# List of numbers
numbers = [1, 2, 3, 4, 5, 6]
# Use filter() to get the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)

#calculate squares for items of numbers list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

mylist = ['111', '22', '3']
mylist = sorted(mylist, key=lambda x: len(x))
print(mylist)

from functools import reduce

"""reduce() - Applies a function of two arguments cumulatively to the elements of an iterable:"""
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

"""max() - Returns the largest item in an iterable or the largest of two or more arguments:"""
data = [(1, 0.4), (2, 0.2), (3, 0.6), (4, 0.1), (5, 0.8)]
max_value = max(data, key=lambda x: x[1])
print(max_value)  # Output: (5, 0.8)

"""min() - Returns the smallest item in an iterable or the smallest of two or more arguments:"""
min_value = min(data, key=lambda x: x[1])
print(min_value)  # Output: (4, 0.1)