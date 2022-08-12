name = input("Whats your name? ")
print("Hey", name + ", welcome to this new adventure!")

answer = input("You are in the end of a labyrinth and see two doors. Choose 'left' or 'right' to pick a door.").lower()

if answer == "left":
    answer = input("You come to a room filled with a lot of pictures. Choose 'big' or 'small' to take it off the wall. ").lower()

    if answer == 'big':
        print("You have found a bag with 5 diamonds")
    elif answer == 'small':
        print("You have found a bag with 13 diamonds")
    else:
        print("Invalid option. You got into a role!")

elif answer == "right":
    answer = input("You see long corridor and a gate that looks like an exit. Choose 'run' or 'back'. ").lower()

    if answer == 'run':
        print("You have found the exit and won the game!")
    elif answer == 'back':
        print("While you are coming back, the corridor collapsed and you are dead.")
    else:
        print("Invalid option. You got into a role!")

else:
    print("Invalid option. You got into a role!")
