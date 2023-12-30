people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

# Filter the list to get people older than 25
filtered_people = [person for person in people if person["age"] > 25]

# Order the list by age
ordered_people = sorted(people, key=lambda person: person["age"])

# Filter and order in one line
ordered_filtered_people = sorted((person for person in people if person["age"] > 25), key=lambda person: person["age"])

# you can use list comprehensions, generator expressions, and built-in functions like:
# filter(), map(), and reduce() for querying and manipulating data.

