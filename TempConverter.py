# Temperature Converter
# Celcius to Fahrenheit &
# Fahrenheit to Celcius

# function with calculation for
# the converation from C to F
def celcius_to_fahrenheit(celcius):
    return (celcius * 9 / 5) + 32

# function with calculation for
# the converation from F to C
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# function to let user choose
# what converter they want
def temp_converter():
    print (f"Welcome to the Temperature converter application")

    print (f"Choose the conversion option you would like to use:")

    print (f"1. Celcius to Fahrenheit")
    print (f"2. Fahrenheit to Celcius")

    # Let user enter an option
    con_temp = input("Enter your option: ")

    # let the user choose from the option
    if con_temp == "1":

        # if user option = 1 then it will let the user input the temperature in celcius
        # the user inputs the temperature in C
        celcius = float(input("Enter the temperature in Celcius: "))

        # it calls the function celcius_to_fahrenheit
        # and assigns the C input by the user for the calculation
        fahrenheit = celcius_to_fahrenheit(celcius)

        # it prints the value of C and let it equal to the value in F after the calculation
        print(f"{celcius} C is equal to {fahrenheit} F.")

    elif con_temp == "2":

        # if the user option = 2 then it will let the user input the temperature in Fahrenheit
        # the user inputs the temperature in F
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

        # it calls the function fahrenheit_to_celcius
        # and assigns the F input by the user for the calculation
        celcius = fahrenheit_to_celcius(fahrenheit)

        # it prints the value the value of F and let it equal to the value in C after the calculation
        print(f"{fahrenheit} F is equal to {celcius} C.")
    else:
        # if the user inputs an option different from 1 or 2,
        # it will print a message to enter a valid option
        print ("Please enter a valid option.")

temp_converter()