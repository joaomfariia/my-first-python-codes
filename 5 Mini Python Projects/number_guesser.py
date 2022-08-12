import random

user_number = input("Type a number: ")

if user_number.isdigit():
    user_number = int(user_number)

    if user_number <= 0:
        print("Please, type a number higher than 0!")
        quit()

else:
    print("Please, type a number.")
    quit()

random_num = random.randint(0, user_number)

tries = 0

while True:

    tries += 1
    user_guess = input("\nGuess a new number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please, type a number.")
        continue
    
    if user_guess == random_num:
        print("\nYay, you guessed the number correctly!")
        break
    elif user_guess > random_num:
        print("Choice above the number!")
    else:
        print("Choice below the number!")

print("You got it in " + str(tries) + " tries.\n")