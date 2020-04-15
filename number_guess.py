import random

# Getting Computer's number

# Getting player's number
# Deciding if you guessed correctly
def pick_winner():
    player_guess = input("Please input a number from 1 to 5: \n")
    player_number = int(player_guess)
    computer_number = random.randint(1, 6)

    if player_number <6 and player_number > 0 and player_number == computer_number:
        return "You won!"
        quit
    if player_number <6 and player_number > 0 and player_number > computer_number:
        print("Too high, sorry!")
        print(pick_winner())
    if player_number <6 and player_number > 0 and player_number < computer_number:
        print("Too low, sorry!")
        print(pick_winner())
    if player_number < 1 or player_number > 5:
        print("Error! Please pick a number from 1 to 5!")

print(pick_winner())