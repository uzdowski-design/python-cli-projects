# START OR STOP THE CAR

# The CLI game to start or stop the car using text commands.

# Creating custom commands and taking basic input.


print("\nWelcome to the most exciting car game ever!")
print("If you are stuck - type 'help'\n")

active = True
car_moving = False

while active:
    command = input('>')
    if command.lower() == 'help':
        print("""Possible commands:
'start' - to start the car
'stop' to stop the car
'quit' to quit the game""")
    elif command.lower() == 'start':
        if car_moving == True:
            print('Car is already started.')
        else:
            print('You started the car.')
            car_moving = True
            # print(car_moving)
    elif command.lower() == 'stop':
        if car_moving == True:
            print('You stopped the car.')
            car_moving = False
        else:
            print('Car is already stopped.')
    elif command.lower() == 'quit':
        print('You quit the game.')
        active = False
    else:
        print("Incorrect command. Type 'help' if you are stuck.")

print('\nThanks for playing!\n')
