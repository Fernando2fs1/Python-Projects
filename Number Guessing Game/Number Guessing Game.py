# Number Guessing Game
import random  #import random lib to automatically give a random numnber
def welcome():

    # while loop to rerun the game if the player chooses to
    while True:
        # print a welcome message to player
        print(f"Welcome to Number Guessing Game") 
        # message to enter 1 to start and 0 to exit the game
        print(f"To start the game please enter 1 to exit please enter 0")
        # variable that will let player input a number 0 or 1 to start the game or exit
        menuOption = input("Enter your option: ")
        # variable defined for random from 1-10
        number_to_guess = random.randint(1, 10)
        # variable that return a boolean value to check if the guess was correct or not
        guess_correct = False
        # variable that returns an int for the number of the times it was needed to guess the number
        attempts = 0

        # if statment that will start the game if the press enter 1 for the menuOption
        if menuOption == "1":
            print(f"Brief explanation: ")
            print(f"enter a number between 1-10")
            print(f"and try to guess the number the system generated.")
            print(f"you will have 3 attempts to guess the number")
            print(f"Lets start the Game:")
            
            while not guess_correct:
                try:
                    guess = int(input(f"Enter your guess: "))
                    attempts += 1

                    if guess < number_to_guess:
                        print(f"The number is too low, try again.")

                    elif guess > number_to_guess:
                        print(f"The number is too high, try again.")

                    else:
                        guess_correct = True
                        print(f"Congratulations, you guessed the number in {attempts} attempts.")

                except ValueError:
                    print("Please enter a number.")

        # else if the user enters 0 it prints the a message and calls the exit method
        elif menuOption == "0":
            print("Thank you for playing")
            exit()
        # if the user enters a number different from 1 or 0 it will print a message that the option is invalid and ask if they would like to play again
        else:
                print(f"Please enter a valid option")

        # if the player enter y for the input on the again variable the game will restart,
        # if the player enters n the game will terminate
        again = input("Would you like to play again? (y/n): ")
        if again == "n":
            break
welcome()
