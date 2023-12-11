# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class ShinyNew(object):
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def show_attributes(self):
        print(self.a, self.b)


def print_funcs():
    print(__name__ == 'funcs')
    obj = ShinyNew(2, 3)
    print(dir(obj))
    print(type(dir(obj)[-2]))


# Press the green button in the gutter to run the script.
if __name__ == '__funcs__':
    print_funcs()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

