print(list(range(12, 101, 8)))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

arrayOfOneBand = ['tic', 'tac', 'toe']
for i, v in enumerate(arrayOfOneBand):
    print(i, v)

count = 0
while count < 3:
    print(f"The count is {count}")
    count += 1

for i in range(1, 10):
    if i == 3:
        continue
    print(i)
    if i == 7:
        break
    else:
        print("else")   # this will not be printed if break is executed in the previous line
           
