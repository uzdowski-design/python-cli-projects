# GUESS THE NUMBER

# Simple CLI game to guess the secret namber using text input.


import random
secret_number = random.randint(1, 101)  # different number everythime
attempts = 0
won = False
print('\nTry to guess the secret number in range between 1 and 100!\n')
while won == False:
    number = int(input('Your guess: '))
    attempts += 1
    if number < secret_number:
        print(f"It's more than that.\n")
    elif number > secret_number:
        print(f"It's less than that.\n")
    else:
        if(attempts < 2):
            print(f"\nAmazing! You guessed with your first attempt!\n")
        else:
            print(f"\nCorrect! You guessed in {attempts} attempts!\n")
        won = True
