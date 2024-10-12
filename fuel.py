def main():
    try:
       fraction = input("enter your balance in fraction: ")
       f = convert(fraction)
       print(f)
    except ValueError:
       print(fraction)
    except ZeroDivisionError:
       print(fraction)


def convert(fuel):
    X,Y = map(int,fuel.split("/"))
    if Y == 0:
        return "denominator cannot be zero"
    # if X >= Y:
    #     return input("enter your balance in fraction: ")
    percentage = round((X/Y)* 100)
    if percentage <= 1:
             return "E"
    elif percentage >= 99:
             return "F"
    else:
      return str(percentage) + "%"


main()

             