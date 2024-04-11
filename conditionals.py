# answer = input("Would you love a bowl of rice? ").lower()


# if answer == "yes":
#     print("Take a bowl.")
# elif answer == "no":
#     print("Ok, I'll just keep  it then.")
# else:
#     print("hmmmmmm!")


# answer = input("Gender: ").upper()

# if answer == "BOY":
#     print("Male")
# elif answer == "GIRL":
#     print("Female")
# elif answer == "BOY AND GIRL":
#     print("Gay")
# else: 
#     print("Guy, choose one! Boy or Girl!")


# SPLIT

first, second, third = input("Give me an input. ").split(" ")

if second == "+":
    answer= int(first) + int(third)
    print(answer)
else:
    print("This symbol does not exist")