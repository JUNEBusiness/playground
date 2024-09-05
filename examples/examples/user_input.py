
# collects a secret from user
secret = input('Tell me a secret, I promise I will not tell anyone: ').lower()
# asks if the user wants the program to divulge the secret
input("You wanna hear a secret?")
# asks if the user is a boy or girl and stores the return value in a variable called gender
gender = input("Are you a boy or a girl?: ").lower()
print(gender)
print()
# sets a condition to divulge the secret
if gender == "Boy" or gender == "boy":
    # prints the secret if the user is a boy
    print(secret)
else:
    # does not divulge the secret if the user is a girl
    print("Oooops!!! I can't tell you, it's a secret")


