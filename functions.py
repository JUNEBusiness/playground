"""Strings(str): These are characters or a set of characters and are denoted or written with quotation marks(single, or double): 'gone'
    "maiden", "Ae125"
    Integers(int): They basically refer to numbers on the real number line: 1, 3, 2424,3546
    Floats(float): They are what you know as decimal point numbers: 1.223,353.345,2424.0000
    Booleans(bool): This is just a true or false statement: True, False. They are used to write conditional statements
    Null(None):None
    
    ...

    Functions: A function is a blackbox that performs a task and returns a value; it has the head, body and the return value
    def cat():
        pass
        return value
    

    cat()   

    dgdgafg
    
    """


# 'Justice while taking the class offered the common eulogy "Here we go again!"'

# 12324
# 12.212
# False
# True
# None

# candle = 'Jacob'
# candle = "musa"

# gives a side effect reaction in the terminal
# print("Hello, World", "1236")

# used to collect input from the user through the terminal
# password = input("Type in your password: ")
# password1 = None
# print(password)
# print(password1)


# def cat():
#     print("meow")
#     return True


# cat()

number = int(input("How many times should the cat meow? "))
# '2'
# int('2')

# def cat(n):
#     for i in range(n):
#         print("meow")
#     # streak = "meow " * n
#     # return streak
# cat(number)

def cat(n):
    streak = "meow \n" * n
    return streak


print(cat(number))