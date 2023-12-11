# This is a sample Python script.
# import tuples
# import lists
# import dicts
# import funcs
# import PandasExamples
import numericpy as np


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    A = [1,2,3]
    A.sort()
    print(type(set(A)))
    print('1,2,3,4'.split(','))
    print(11 // 2)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    name = '1234567'
    print(name[::2])
    print(11 // 2)
    print(len(name))
    print(name[0:7:3])
    print(name[0:7])
    print(name[::3])
    name = "Michael Jackson"

    # Use single quotation marks for defining string
    name = 'Michael Jackson'

    # Find the length of string
    len("Michael Jackson")

    # Digitals and spaces in string
    '1 2 3 4 5 6 '

    # Print the last element in the string
    print(name[-1])

    print(name[-15])

    # Take the slice on variable name with only index 0 to index 3
    name[0:4]

    # Take the slice on variable name with only index 8 to index 11
    name[8:12]

    # Get every second element in the range from index 0 to index 4
    name[0:5:2]

    # Get every second element. The elments on index 1, 3, 5 ...
    name[::2]

    # Concatenate two strings

    statement = name + "is the best"
    statement

    # Print the string for 3 times
    3 * "Michael Jackson"

    # New line escape sequence
    print(" Michael Jackson \n is the best")

    # Tab escape sequence
    print(" Michael Jackson \t is the best")

    # Include backslash in string
    print(" Michael Jackson \\ is the best")

    # r will tell python that string will be display as Raw string
    print(r" Michael Jackson \ is the best")

    # Convert all the characters in string to upper case

    a = "Thriller is the sixth studio album"
    print("before upper:", a)
    b = a.upper()
    print("After upper:", b)

    # Replace the old substring with the new target substring is the segment has been found in the string

    a = "Michael Jackson is the best"
    b = a.replace('Michael', 'Janet')
    b

    # Find the substring in the string. Only the index of the first elment of substring in string will be the output

    name = "Michael Jackson"
    name.find('el')
    print(type(int(12.3)))
    print(int(True))
    print(type(2 / 2))
    L = (1, 3, 2)
    sorted(L)
    print(L)


"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Use quotation marks for defining string

# print_hi('test')
# tuples.print_hoi()
# lists.print_hallo()
# dicts.print_dict()
# funcs.print_funcs()
# PandasExamples.dict_data_frame()
np.numpy_lib()
