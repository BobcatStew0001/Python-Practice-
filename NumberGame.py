#Simple Number Guessing Game
import random #Generate random number
computer_guess = random.randint(1,10) #Store in a variable

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
        print("Guess Again")