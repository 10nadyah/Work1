import random

counter = 0
value = 1

coinarray = ["heads", "tails"]

while value > counter:
    print(random.choice(coinarray))
    counter += 1