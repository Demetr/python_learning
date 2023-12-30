for i in range(10):
    print(i)
    x = i * 2
    print(x)

for i in range(6):
    if i == 3:
        continue
    print(i)

count = 0
while count < 3:
    print(f"count = {count}")
    count += 1

while True:
    print(f"count = {count}")
    if count == 5:
        break
    count += 1

thinkers = ["Plato", "PlayDo", "Gumby"]
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print("We tried to pop too many thinkers")
        print(e)
        break
    except IOError as e:
        print("IOError")
        print(e)
        break
    except KeyError as e:
        print("KeyError")
        print(e)
        break
    except ImportError as e:
        print("ImportError")
        print(e)
        break

class FancyCar():
    pass

type(FancyCar)
my_car = FancyCar()
type(my_car)


class ShinyNewFancyCar : FancyCar
wheels = 4
def driveFast(self):
    print("Driving fast")

my_car = ShinyNewFancyCar()
my_car.driveFast()

# in and notin
2 in [1, 2, 3]
'a' not in 'cat'
10 in range(10)
1 not in range(2,4)

my_sequnce = "Bill Cheathman"
my_sequnce.index('C')
my_sequnce.index('l')
my_sequnce[4]

my_sequnce[-6:]
my_sequnce[3:]

min(my_sequnce)
max(my_sequnce)
len(my_sequnce)
my_sequnce.count(1)

newList = list(range(10))
newList.append(10)
newList.insert(0, -1)
newList.extend([11, 12, 13])
newList.pop()

squeres= []
for i in range(10):
    squeres.append(i**2)

squeres = [i**2 for i in range(10)]
squeres = [i**2 for i in range(10) if i%2 == 0]
