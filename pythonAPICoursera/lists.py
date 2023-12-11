# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hallo():
    # Use a breakpoint in the code line below to debug your script.
    print("start lists")
    say_what = ['say', 'what', 'you', 'will']
    A = [1]
    A.append([2, 3, 4, 5])
    #say_what.extend([0, 1, 2])
    #print('ex:'+say_what)
    #say_what.append(['a', 'b', 'c'])
    print('ap:')
    print(A)

    print(say_what)
    print(type(say_what))

    print("Hello Mike".split())
    list_old = "A,V,A,D,E".split(",")
    print(list_old)
    list_new = list_old[:]
    list_old[0] = "B"
    print(list_old)
    print(list_new)
    list_newest = list_old + list_new
    print(list_newest)

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

