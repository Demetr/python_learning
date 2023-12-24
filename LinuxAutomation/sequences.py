2 in [1,2,3]
# True

'a' not in 'cat'
# False

10 in range(12)
# True

10 not in range(2,4)
# True

my_sequence = 'Bill Cheatham'
my_sequence[0]
# 'B'
my_sequence[2]
# 'l'
my_sequence[12]

my_sequence[0:4]
# 'Bill'

my_sequence[5:len(my_sequence)]

my_sequence[-1]
# 'm'

my_sequence[-2]
# 'a'

my_sequence[-len(my_sequence)]
# 'B'

my_sequence.index('C')
# 5
my_sequence.index('a')
# 8
my_sequence.index('a', 9, 12)
# 11

my_sequence[11]
# 'a'

# slicing my_sequence[start:stop:step]
my_sequence[0:12:2]
# 'BlCeat'
my_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_sequence[2:5]
# ['c', 'd', 'e']
my_sequence[:5]
# ['a', 'b', 'c', 'd', 'e']
my_sequence[3:]
# ['d', 'e', 'f', 'g']

my_sequence[-6:]
# ['b', 'c', 'd', 'e', 'f', 'g']
my_sequence[3:-1]
# ['d', 'e', 'f']

my_sequence = [0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]
len(my_sequence)
# 12
min(my_sequence)
# 0
max(my_sequence)
# 4
my_sequence.count(1)
# 3

