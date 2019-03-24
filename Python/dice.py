import random

dValue = 1
counter = 0
dicearray = [1, 2, 3, 4, 5, 6]

while dValue > counter:
    print(random.choice(dicearray))
    counter += 1