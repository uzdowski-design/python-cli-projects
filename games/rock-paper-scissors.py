# ROCK - PAPER - SCISSORS

# Do you have what it takes to outsmart your computer?


from random import randint

# Welcome message
print('')
print('Welcome to the classic game "Rock - Paper - Scissors"!')
print('Do your best and try to outsmart your computer.')
print('')

# global variables
choices = ['rock', 'paper', 'scissors']
ai_score = 0
player_score = 0
message = ''
game_over = False
ai_choice = None
player_choice = None
winner_msg = None
win_score = 3

# reset game stats


def reset_game():
    global ai_score
    global player_score
    global message
    global game_over
    global ai_choice
    global player_choice
    global winner_msg
    ai_score = 0
    player_score = 0
    message = ''
    game_over = False
    ai_choice = None
    player_choice = None
    winner_msg = None


def make_choices():
    global ai_choice
    global player_choice
    # generate random AI choice
    ai_choice = randint(0, 2)
    # get player choice
    player_choice = int(
        input('Make your choice (1 - rock, 2 - paper, 3 - scissors): ')) - 1


# check results, add score and assign round winner
def check_result(player_choice, ai_choice):
    global message
    global ai_score
    global player_score
    if player_choice == ai_choice:
        message = 'Tie.'
        return
    elif player_choice == 0:
        if ai_choice == 1:
            message = 'Computer wins.'
            ai_score += 1
            return
        else:
            message = 'You win!'
            player_score += 1
            return
    elif player_choice == 1:
        if ai_choice == 0:
            message = 'You win!'
            player_score += 1
            return
        else:
            message = 'Computer wins.'
            ai_score += 1
            return
    elif player_choice == 2:
        if ai_choice == 1:
            message = 'Computer wins.'
            ai_score += 1
            return
        else:
            message = 'You win!'
            player_score += 1
            return

# check final winner


def check_final_winner():
    global winner_msg
    if player_score >= win_score or ai_score >= win_score:
        if player_score > ai_score:
            winner_msg = 'You rock! Smashed it like a pro!'
            return True
        else:
            winner_msg = 'You suck! Try harder next time...'
            return True
    else:
        return False


# play the game
def play_game():
    reset_game()
    global game_over
    while game_over == False:
        make_choices()
        check_result(player_choice, ai_choice)
        print('')
        print('('+str(player_score) + ') Your choice: ' +
              choices[player_choice])
        print('('+str(ai_score) + ') Computer\'s choice: ' +
              choices[ai_choice])
        print(message)
        print('')

        if check_final_winner() == True:
            print(winner_msg)
            print('')
            game_over = True
            play_again = input(
                'Wanna play again? (press \'Y\' to continue): ')
            print('')
            if play_again.lower() == 'y':
                play_game()


play_game()
