import random
print("Welcome to the Hangman Game!")
print("The theme of today's word search is fruits and vegetables")
print("Rules: Each Player will get 4 turns to either guess the word or a letter.\nAfter a Players turn the next Player will then have the option to solve it.")
print("If a correct guess is made either letter or the word then a 'Correct!' message will be displayed.")
print("if an incorrect guess is made then a 'Wrong!' message will be displayed.")

player1 = input("Player 1 Enter your name:")

player2 = input("Player 2 Enter your name: ")

players = [player1, player2]

word_list = ["apple", "pear", "tomato", "coffee", "pickle", "carrot", "potato"]

chosen_word = random.choice(word_list).lower()

solved = False

for _ in range(4):
    for player in players:
        option = input(f"{player} Would you like solve the puzzle? Y/N").upper()
        if option == "Y":
            puzzle_guess = input("Enter your guess: ")
            if puzzle_guess == chosen_word:
                print("Correct!")
                solved = True
                break
            else:
                print("Wrong!")
        else:
            letter_guess = input("Enter a letter:").lower()
            if letter_guess in chosen_word:
                print("Correct!")
            else:
                print("Wrong!")
    if solved == True:
        break

