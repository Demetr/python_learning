iAmEmptyList = list()
print(iAmEmptyList)
print(len(iAmEmptyList))

iAmListOf10Digits = list(range(10))
print(iAmListOf10Digits)
print(len(iAmListOf10Digits))

iAmListOfHenryMiller = list('Henry Miller')
print(iAmListOfHenryMiller)
print(len(iAmListOfHenryMiller))

iAmEmptyList = []
iAmEmptyList

nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nine

mixed = [0, 'one', 2, nine, 4, 'five', 6, 'seven', 8, 'nine']
mixed

pies = ['cherry', 'apple']
pies

pies.append('rhubarb')
pies

pies.insert(1, 'blueberry')
pies

desserts = ['cookies', 'cake']
desserts.extend(pies)
desserts

pies.pop()
pies

pies.pop(1)
pies

desserts
desserts.remove('cookies')
desserts

squares = []
for x in range(10):
    squares.append(x**2)
squares

# comprehensions 
squares = [x**2 for x in range(10)]
squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# comprehensions with conditionals
squares = [x**2 for x in range(10) if x % 2 == 0]
squares
# [0, 4, 16, 36, 64]


