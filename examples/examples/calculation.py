""" 0 degrees Celcius === 32 degrees Fahrenheit
To convert from degree Celcius to degree Fahrenheit we use (X°C * 9/5) + 32 = XF
"""

def main():
    celcius = input("Give me a temperature in °C: ")
    fahrenheit = cel_to_fah(celcius)
    # prints out fahrenheit value and fahrenheit type
    print(f"Fahrenheit: {fahrenheit}, Type: {type(fahrenheit)}")

# converts degree celcius to fahrenheit
def cel_to_fah(deg_celcius):
    # does the calculation and store its value in fahrenheit_val
    fahrenheit_val = (int(deg_celcius) * 9/5) + 32
    # returns fahrenheit value
    return fahrenheit_val

main()
