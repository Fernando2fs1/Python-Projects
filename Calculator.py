# Calculator

# Function defined as Calculator to perform the calculations
def Calculator():

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

    if operationChoice == "1":
        print(f"The result of {a} + {b}  is:  {a + b}")

    elif operationChoice == "2":
        print(f"The result of {a} - {b} is: {a - b}")

    elif operationChoice == "3":
        print(f"The result of {a} + {b} is: {a * b}")

    elif operationChoice == "4":
        print(f"")


Calculator()