# TIC TAC TOE

# Simple CLI implementation of a popular game.


# ---------- Global Variables -----------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# Positions guide board
board_positions = ["1", "2", "3",
                   "4", "5", "6",
                   "7", "8", "9"]

# Check if game still going
game_still_going = True

# Who won / tie
winner = None

# Whose turn is it
curr_player = "X"

# Display board


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Display positions board


def display_board_positions():
    print(board_positions[0] + " | " +
          board_positions[1] + " | " + board_positions[2])
    print(board_positions[3] + " | " +
          board_positions[4] + " | " + board_positions[5])
    print(board_positions[6] + " | " +
          board_positions[7] + " | " + board_positions[8])

# Handle a single turn of an arbitrary player


def handle_turn(player):
    print(player + "'s turn.")
    position = input('Choose a position from 1-9: ')

    # Validate input
    valid = False
    while not valid:
        # if input invalid ask for input again
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input('Choose a position from 1-9: ')
        position = int(position) - 1

        # Check if position not taken
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    # Take position
    board[position] = player
    # Display board again
    display_board()

# Check if the game has ended


def check_if_game_over():
    check_for_winner()
    check_if_tie()

# Check for the winner


def check_for_winner():
    # Assign this variable to global winner variable
    global winner
    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    # Assign winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# Check rows def


def check_rows():
    # Set up global variables
    global game_still_going
    # Check if any of the rows are equal (win)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # Change game_still_going if any is true
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[3]
    return

# Check columns def


def check_columns():
    # Set up global variables
    global game_still_going
    # Check if any of the columns are equal (win)
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # Change game_still_going if any is true
    if col_1 or col_2 or col_3:
        game_still_going = False
    # Return winner (X or O)
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

# Check diagonals def


def check_diagonals():
    # Set up global variables
    global game_still_going
    # Check if any of the diagonals are equal (win)
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    # Change game_still_going if any is true
    if diag_1 or diag_2:
        game_still_going = False
        # Return winner (X or O)
        return board[4]
    return

# Check if result is tie


def check_if_tie():
    # Set up global varbiable
    global game_still_going
    # If no more blank spaces on the board end game
    if "-" not in board:
        game_still_going = False
    return

# Flip player turn def


def flip_player():
    # Set global variable
    global curr_player
    # Change player
    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"
    return

# Play the game def


def play_game():
    # Welcome message
    print('Welcome to the TIC-TAC-TOE game.')
    print('Chose position according to the below template:')
    # Display board positions guide
    display_board_positions()
    print('')
    # Display initial board
    display_board()
    # While the game is still going
    while game_still_going:
        # Hande a single turn of an arbitrary player
        handle_turn(curr_player)
        # Check if the game is over
        check_if_game_over()
        # Change player turn
        flip_player()
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# initialize the game
play_game()
