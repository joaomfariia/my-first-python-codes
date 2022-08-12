import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type: Rock/Paper/Scissors or 'Q' to quit: ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        print("\nType a correct option!\n")
        continue

    random_num = random.randint(0, 2)
    # rock = 0  paper = 1  scissors = 2

    computer_pick = options[random_num]
    print("\nComputer picked", computer_pick + " and you picked", user_input)
    
    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!\n")
        user_wins += 1
        
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!\n")
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won!\n")
        user_wins += 1
        
    elif user_input == computer_pick:
        print("Draw!!\n")
        continue

    else:
        print("You lost!\n")
        computer_wins += 1

if computer_wins == 3:
    print("The computer is the winner.")
    quit()

elif user_wins == 3:
    print("You are the winner!")
    quit()