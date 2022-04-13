isJoke = input("Do you wanna read a joke?").lower()

# lower() will lowerCase the strings

print(isJoke)

if isJoke == "yes":
    print("It's my joke")
if isJoke == "no": # worked same as elif
    print("No")
if isJoke == "dibas": # worked same as elif
    print(isJoke)
else:
    print("you denied :(")

# if..else
# if...elif...else