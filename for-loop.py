the_cont = [1, 2, 3, 4, 5]
stocks = ["APPL", "GOOGL", 'TSLA']
random_things = ["Puppies", 26, "Baby", "😍", 1/2, ["One", "two"]]


for number in the_cont:
    print(f"This is count {number}")


for random in random_things:
    print(f"It's random {random}")

# let's build a list programmatically
people = []

people.append("Ram")
people.append('Sham')
people.append('Krishna')

people.remove('Sham')

print(people)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# number is the variable that we assign
for number in numbers:
    square = number * number
    print(square)

# cleaner way
for number in range(1,10):
    square = number * number
    print(f"{number} squared is {square}")