# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Adding an element to a set:
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Removing an element from a set
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Checking if an element is in a set
print("apple" in fruits)  # Output: True