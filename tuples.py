"""Tuples are just like lists, but use brackets, not square brackets"""
fruits = ("Apple", "Mango", "Banana", 'Watermelon', "Orange", "Beetroot", 6)

# for fruit in fruits:
#     print(fruit)

"""Tuples are immutable, i.e its values cannot be overwritten. It will throw an error"""

fruits[0] = "Plum"

for fruit in fruits:
    print(fruit)