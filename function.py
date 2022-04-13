# def stands for definition, we defined new function named greet

def greet(name):
    print(f"Hello, {name}!")

greet("Dibas")

# another function
def age_in_dog_years(age):
    return age * 7
   
print(age_in_dog_years(19))

# two arguments
def concat(word1, word2):
    print(f"Hi {word1} {word2}")

concat("Dibas", "Dauliya")
concat(word2="Dibas", word1="Dauliya") # assigning specific value


# CHALLENGE
def uppercase_and_reverse(word):
    return word.upper()[::-1]

print(uppercase_and_reverse("dibas"))

# another method
def reverse(word):
    return word[::-1]

def uppercase_and_reverse(word):
    return reverse(word.upper())

print(uppercase_and_reverse("another"))