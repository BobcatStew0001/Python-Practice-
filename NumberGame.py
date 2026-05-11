import random
import time
print("Hello my name is Anton")
player_name = input("What is your name? ").capitalize()
play_game = input(f"Hello {player_name} would you like to play a number guessing game? Y or N? ").upper()
computer_guess = random.randint(1, 10)
if play_game == "Y":
    for i in range(3, 0,-1): #Number in () is number of guesses
        guess = int(input("Guess a number between 1 and 10?"))
        if guess == computer_guess:
            print("Congratulation!! You Win")
            break #stops the game with a correct guess
        elif guess > computer_guess:
            print("You're too high")
            print(f"You have {i - 1} guesses left")
        elif guess < computer_guess:
            print("You're too low")
            print(f"You have {i - 1} guesses left")
    else:
        print("You're out of guesses")
        print("\033[91m"+"The number I was thinking of was " + str(computer_guess) +"\033[0m")
else:
    print("Come back when you're ready to play with me.")