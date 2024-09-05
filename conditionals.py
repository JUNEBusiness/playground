# If there is fuel, start the car
#     if there is no fuel, don't start the car

#     If there is fuel:
#         start the car
#     if there is no fuel:
#         don't start the car

#     is there fuel?
#     if "Yes":
#         start the car
#     if "No":
#         don't start the car

#     if "Yes":
#         print('start the car')
#     if "No":
#         print('don't start the car')


# answer = input("Will you be my friend: ").lower()

# if answer == "yes":
#     print("great! I would love to be your friend also!")

# if answer == "no":
#     print("Ok! and I want to be your friend.")

# if answer == "maybe":
#     print("I will wait for you to decide.")


# y = input("What is the value of y? ")
# x = input("What is the value of x? ")

# if x > y or x < y:
#     print("X is not equal to Y")
# else:
#     print("X is equal to Y")


# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# def main():
#     answer = is_even(int(input("Give me a number: ")))
#     if answer:
#         print("This number is even")
#     else:
#         print("This number is odd")


# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# main()

# def main():
#     answer = is_even(int(input("Give me a number: ")))
#     if answer:
#         print("This number is even")
#     else:
#         print("This number is odd")


# def is_even(x):
#      return True if x % 2 == 0 else False

# main()


# name = input("What's your name? ").title()

# if name == "Abayomi" or name == "Dupe":
#     print("Yoruba")
# elif name == "Funke":
#     print("Yoruba")
# elif name == "Hilkiah":
#     print("Igbo")
# elif name == "Sanusi":
#     print("Hausa")
# else:
#     print("Who?")

# name = input("What's your name? ").title()

# match name:
#     case "Abayomi" |"Dupe" | "Sade" | "Funke":
#         print("Yoruba")
#     case "Hilkiah" | "Chidalu" | "Emeka" | "Nnamdi":
#         print("Igbo")
#     case "Sanusi" | "Usman" | "Boris" | "Danlamin":
#         print("Hausa")
#     case _:
#         print("Who?")
