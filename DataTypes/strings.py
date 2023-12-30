string = str()
# string = ''


# string constructor to make string from other objects
my_list = list()
str(my_list)
# '[]'

#multiline string
multi_line = """This is a
 multi-line string,
 which includes linebreaks.
 """
print(multi_line)

# inputString = input("Enter a string: ")
# print(inputString)  # inputString is a string

input = "  I want more   "
input.strip()
# 'I want more'

input.rstrip()
# '  I want more'

input.lstrip()
# 'I want more   '

output = 'Barry'
output.ljust(10)
# 'Barry     '

output.rjust(10, '*')
# '*****Barry'

output.center(10, '*')
# '**Barry***'

output.zfill(10)
# '00000Barry'

text = "Marty had a little lamb"
text.split()
# ['Marty', 'had', 'a', 'little', 'lamb']

url = "https://gt.motomomo.io/v2/api/asset/143"
url.split('/')
# ['https:', '', 'gt.motomomo.io', 'v2', 'api', 'asset', '143']

items = ['cow', 'milk', 'bread', 'butter']
" and ".join(items)
# 'cow and milk and bread and butter'

name = "bill monroe"
name.capitalize()
# 'Bill monroe'

name.uppper()
# 'BILL MONROE'

name.title()
# 'Bill Monroe'

upperCase = name.swapcase()
# 'BILL MONROE'
name.title().swapcase()
# 'bILL mONROE'

upperCase.lower()
# 'bill monroe'

"William".startswith("W")
# True
"William".startswith("Bill")
# False
"Molly".endswith("olly")
# True
"abc123".isalnum() # alphanumeric and string is at least one character
# True
"abc123".isalpha() # alphabetic and string is at least one character
# False
"abc".isalnum()
# True
"123".isnumeric() # numeric and string is at least one character
# True
"Sandy".istitle()
# True
"Sandy".islower()
# False
"SANDY".isupper()
# True

#old C formatting like printf
"%s + %s = %s" % (1, 2, "Three")
# '1 + 2 = Three'

#conversion specifier
"%.3f" % 1.23456789
# '1.235'

# String format method
print("Hello, {}. You are {} years old.".format("Alice", 25))
print('''{country} is an island.
... {country} is off of the coast of
... {continent} in the {ocean}'''.format(ocean='Indian Ocean',
                                      continent='Africa',
                                      country='Madagascar'))
values = {'first': 'Bill', 'last': 'Bailey'}
print("Won't you come home {first} {last}?".format(**values))
#"Won't you come home Bill Bailey?"

# left and right padding
text = "|{0:>22}||{0:<22}|"
text.format('O','O')
#'|                     O||O                     |'
text = "|{0:<>22}||{0:><22}|"
text.format('O','O')
#'|<<<<<<<<<<<<<<<<<<<<<O||O>>>>>>>>>>>>>>>>>>>>>|'

# f-strings
a = 1
b = 2
f"a is {a}, b is {b}. Adding them results in {a + b}"
#'a is 1, b is 2. Adding them results in 3'

count = 43
f"|{count:5d}"
#'|   43'

padding = 10
f"|{count:{padding}d}"
#'|        43'


from string import Template # string templates

t = Template('Hello, $name. You are $age years old.')
s = t.substitute(name='Alice', age=25)
print(s)
# Output: 'Hello, Alice. You are 25 years old.'# Output: 'Hello, Alice. You are 25 years old.'
# internationalization example
greeting = Template("$hello Mark Anthony")
greeting.substitute(hello="Bonjour")
'Bonjour Mark Anthony'
greeting.substitute(hello="Zdravstvuyte")
'Goedemiddag Mark Anthony'
greeting.substitute(hello="Nǐn hǎo")
'Nǐn hǎo Mark Anthony'

