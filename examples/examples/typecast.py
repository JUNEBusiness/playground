
""" The input function works in a way that, no matter the input you give it in the terminal,
either String (Str) or Float or Integer (int), it will always give a string as its return value."""

# value is a string in this line
value = input("Give me a value: ")
# numero is a int in this line
numero = 1

""" The function int(), str(), and float() helps to change the class of a variable
int() changes the variable to an integer and leaves it the same if it is aleady an innteger
str() changes the variable to a string and leaves it unchanged if it is already a string
float() changes the variable to a floating point number/decimal and leaves it unchanged if it is already a float0"""
# change the type/class of "value" to an int from a string
value_typecast = int(value)

# change the type/class of "numero" to a string from an intetger
numero_typecast = str(numero)

# prints out the class of each variable
print(f"Value: {type(value)}, Numero: {type(numero)},\
        value_typecast: {type(value_typecast)}, \
        numero_typecast: {type(numero_typecast)} ")

