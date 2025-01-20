# Calculator

# Function defined as Calculator to perform the calculations
def Calculator():
    #this allows the user to try again
    while True:
        # Calculator introduction
        print ("Welcome to My Python calculator project.")

        # take the input from the user
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        # Display calculation option
        print ("Choose an operation:")
        print ("1  - addition")
        print ("2  - subtraction")
        print ("3  - multiplication")
        print ("4  - division")

        # This take the user's operation choice
        operationChoice = input("Enter the number for the operation you wish to perform: ")



        # This will perform the operation chosen by the user
        if operationChoice == "1":
            print(f"The result of {a} + {b}  is:  {a + b}")

        elif operationChoice == "2":
            print(f"The result of {a} - {b} is: {a - b}")

        elif operationChoice == "3":
            print(f"The result of {a} + {b} is: {a * b}")

        elif operationChoice == "4":
            if b != 0:
                print ( f"The result of {a} / {b} is: {a / b}")
            else:
                print("Error!!")
        else:
            print ("Invalid Choice option.")

        again = input ("Would you like to perform another operation? (y/n): ")
        if again != "y":
            break

Calculator()