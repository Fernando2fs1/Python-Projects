# Number Guessing Game
import random
def welcome():

    while True:
        print(f"Welcome to Number Guessing Game")
        print(f"To start the game please enter 1 to exit please enter 0")
        menuOption = input("Enter your option: ")
        number_to_guess = random.randint(1, 10)
        guess_correct = False
        attempts = 0

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

        elif menuOption == "0":
            print("Thank you for playing")
            exit()
        else:
                print(f"Please enter a valid option")

        again = input("Would you like to play again? (y/n): ")
        if again == "n":
            break
welcome()
