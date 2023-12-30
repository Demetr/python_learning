# sample dictionary
map = dict()
type(map)
# <class 'dict'>

kv_list = [['key-1', 'value-1'], ['key-2', 'value-2'], ['key-3', 'value-3']]
dict(kv_list)
# {'key-1': 'value-1', 'key-2': 'value-2', 'key-3': 'value-3'}

map = {'key-1': 'value-1', 'key-2': 'value-2', 'key-3': 'value-3'}
map
# {'key-1': 'value-1', 'key-2': 'value-2', 'key-3': 'value-3'}

map['key-1']
# 'value-1'

map['key-2']
# 'value-2'

map['key-4'] = 'value-4'
map
# {'key-1': 'value-1', 'key-2': 'value-2', 'key-3': 'value-3', 'key-4': 'value-4'}
map['key-1'] = 12
map
# {'key-1': 12, 'key-2': 'value-2', 'key-3': 'value-3', 'key-4': 'value-4'}

# if you try to access a key that doesn't exist, you'll get a KeyError exception
try:
    map['key-5']
except KeyError as e:
    print('Caught KeyError exception:', e)

#instead use in <dictionary> to check if a key exists
if 'key-5' in map:
    print(map['key-5']+" exists via if-else")
else:
    print("key-5 doesn't exist via if-else")

# a more intuitive solution is to use the get() method
map.get('key-5', 'default value via get()')
# 'default value'
#if you have not defined key in a dict, it returns default value

# use del to remove a key-value pair from a dictionary
del map['key-4'] # or del(map['key-2'])
map.__delitem__('key-2')
map
# {'key-1': 12, 'key-2': 'value-2'}

# keys() returns a list of all the keys in a dictionary a dict_keys object
map.keys()
# dict_keys(['key-1', 'key-2'])

# values() returns a list of all the values in a dictionary a dict_values object
map.values()
# dict_values([12, 'value-2'])

for key, value in map.items():
    print(f"{key}, {value}")
# key-1, 12
# key-3, value-3

# dict comprehensions
# {<expression> for <element> in <sequence>}
    letters = 'abcdefg'
    # mapping individual letters to their upper-case representations
    cap_map = {x: x.upper() for x in letters}
    cap_map['b']
    # 'B'

    cap_map

