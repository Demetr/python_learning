#class Animal(object): Python 2.x
class Animal:
    type = "Animal"

    def __init__(self, color="Grey", size="Small", stripes=False):
        self.color = color
        self.size = size
        self.stripes = stripes

    # declaring __str__() method
    def __str__(self) -> str:
        return "I'm a {} {} {}".format(self.size, self.color, self.type)

    # declaring __repr__() method
    def __repr__(self):
        o = self
        return_str = (f'The creature is {o.size} {o.type}, it is {o.color} and ' +
                      ("has stripes" if o.stripes else "has no stripes"))
        return return_str


class Tiger(Animal):
    type = "Tiger"
    stripes_color = "Brown"

    def __init__(self, color="Orange", size="Medium", stripes=True, stripes_color="Black"):
        super().__init__(color, size, stripes)
        self.stripes_color = stripes_color

    # declaring __repr__() method
    def __repr__(self):
        o = self
        return_str = (f'The creature is {o.size} {o.type}, it is {o.color} and ' +
                      (f"has {o.stripes_color} stripes" if o.stripes else "has no stripes"))
        return return_str

#TODO: What to do with stripes versus spots?
# class Elephant(Animal):
#     type = "Elephant"
#     spots_color = "Brown"
#
#     def __init__(self, color="Orange", size="Medium", spots=True, spots_color="Pink"):
#         super().__init__(color, size, spots)
#         self.spots_color = spots_color
#
#     # declaring __repr__() method
#     def __repr__(self):
#         o = self
#         return_str = (f'The creature is {o.size} {o.type}, it is {o.color} and ' +
#                       (f"has {o.spots_color} stripes" if o.stripes else "has no stripes"))
#         return return_str

def main():
    obj = Animal("Brown", "Large", False)
    print(obj)
    print(str(obj))
    print(repr(obj))

    obj = Tiger()
    print(obj)
    print(str(obj))
    print(repr(obj))

    obj = Tiger("Golden Orange", "Medium", True, "Brown")
    print(obj)
    print(str(obj))
    print(repr(obj))

if __name__ == '__main__':
    main()
