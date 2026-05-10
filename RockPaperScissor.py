import random
import time
player_wins = 0
computer_wins = 0
print("Hello my name is Anton")
time.sleep(2)
player_name = input("What is your name? ").capitalize()
answer = input(f"Hello {player_name}! Would you like to play a Rock Paper Scissors with me? Y/N").upper()
time.sleep(3)
if answer == "Y":
    print("Best 2 out of three")
    for i in range(3):
        print("Great! We throw on the the count of 3. Are you ready?")
        print("1")
        print("2")
        print("3")
        print('go')
        player_move = input("Throw").lower()
        time.sleep(5)
        computer = random.choice(["rock", "paper", "scissors"])
        if computer == "rock" and player_move == "scissors":
            print(f"Sorry {player_name} You Lose!")
            computer_wins += 1
        elif computer == "rock" and player_move == "paper":
            print(f"Way to go {player_name} You Win!")
            player_wins += 1
        elif computer == "paper" and player_move == "scissors":
            print(f"Way to go {player_name} You Win!")
            player_wins += 1
        elif computer == "scissors" and player_move == "paper":
            print(f"Sorry {player_name} You Lose!")
            computer_wins += 1
        elif computer == "scissors" and player_move == "rock":
            print(f"Way to go {player_name} You Win!")
            player_wins += 1
        elif computer == "paper" and player_move == "rock":
            print(f"Sorry {player_name} You Lose!")
            computer_wins += 1
        else:
            print("It's a Draw!")

    print(f"{player_name} {player_wins} - Anton {computer_wins}")
    if player_wins > computer_wins:
        print(f"Congratulations {player_name} You Win!")
    elif player_wins < computer_wins:
        print(f"Sorry {player_name} Better Luck Next time!")
    else:
        print("Let's Play Again!")
else:
    print("Maybe Next Time!")




