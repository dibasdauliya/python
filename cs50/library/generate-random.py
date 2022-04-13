import random
# from random import choice

#WARN: never make same name of file as of import word

coin  = random.choice(["heads", "tails"])
print(coin)

# a and b inclusive
num = random.randint(1, 10)
print(num)

# takes value and randomize
cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)