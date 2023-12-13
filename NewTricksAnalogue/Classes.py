#class Animal(object): Python 2.x
class Animal:
    type = "Animal"
    color = ""
    size = ""

    def __init__(self, color="Grey", size="Small"):
        self.color = color
        self.size = size

    # declaring __str__() method
    def __str__(self) -> str:
        return "I'm a {} {} {}".format(self.size, self.color, self.type)

    # declaring __repr__() method
    def __repr__(self):
        return f'The creature is {self.size} {self.type}, it is {self.color}'


class Tiger(Animal):
    type = "Tiger"
    stripes_color = ""

    def __init__(self, color="Orange", size="Medium", stripes=True, stripes_color="Black"):
        super().__init__(color, size)
        self.stripes = stripes
        self.stripes_color = stripes_color

    # declaring __repr__() method
    def __repr__(self):
        return_str = (f'The creature is {self.size} {self.type}, it is {self.color} and ' +
                      (f"has {self.stripes_color} stripes" if self.stripes else "has no stripes"))
        return return_str


class Elephant(Animal):
    type = "Elephant"
    spots = False
    spots_color = ""

    def __init__(self, color="Greyish Black", size="Large", spots=False, spots_color="Pink"):
        super().__init__(color, size)
        self.spots_color = spots_color
        self.spots = spots

    # declaring __repr__() method
    def __repr__(self):
        return_str = (f'The creature is {self.size} {self.type}, it is {self.color} and ' +
                      (f"has {self.spots_color} spots" if self.spots else "has no spotes"))
        return return_str


def main():
    obj = Animal("Brown", "Large")
    print(obj)
    print(str(obj))
    print(repr(obj))
    print("---------------------")
    obj = Tiger()
    print(obj)
    print(str(obj))
    print(repr(obj))
    print("---------------------")
    obj = Tiger("Golden Orange", "Medium", True, "Brown")
    print(obj)
    print(str(obj))
    print(repr(obj))
    print("---------------------")
    obj = Elephant("Grey", "Large", True, "Pink")
    print(obj)
    print(str(obj))
    print(repr(obj))


if __name__ == '__main__':
    main()