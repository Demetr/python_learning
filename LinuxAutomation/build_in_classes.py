# Define a class for fancy defining fancy cars
class FancyCar():
    pass

type(FancyCar)

# Instantiate a fancy car
my_car = FancyCar()
type(my_car)

class FancierCar(FancyCar):
    # Add a class variable
    wheels = 4
    # Add a method
    def driveFast(self):
        print("Driving so fast!")

my_fancier_car = FancierCar()
my_fancier_car.driveFast()
