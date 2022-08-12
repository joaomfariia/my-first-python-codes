print('Welcome to my Quiz game!')

play = input('Do you want to play? ')

if play == 'yes':
    print("Ok, let's play!")

if play != 'yes':
    print('Ok, bye bye!')
    quit()

score = 0

answer = input("Which year Brazil was discovered? ").lower()
if answer == '1500':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Which native people was found in Brazil? ").lower()
if answer == 'indian' or answer == 'indians':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Which continent Brazil is part of? ").lower()
if answer == 'south america':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the current capital of Brazil? ").lower()
if answer == 'distrito federal':
    print('Correct!')
    score += 1          # score = score + 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' answers correctly!')
