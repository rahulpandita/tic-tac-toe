# Tic Tac Toe
import random

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('---------')
    for i in range(3):
        for j in range(3):
            # Calculate the position number
            position_number = i * 3 + j + 1
            # If the board position is empty, print the position number
            if board[i * 3 + j] == ' ':
                print('|', position_number, end=' ')
            else:
                print('|', board[i * 3 + j], end=' ')
        print('|')
        print('---------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(3):
        if board[i*3] == board[i*3 + 1] == board[i*3 + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()
        if current_player == 'O':  # Computer's turn
            position = random.randint(1, 9)
            while board[position - 1] != ' ':
                position = random.randint(1, 9)
        else:  # Human's turn
            position = int(input('Enter a position (1-9): '))
        if board[position - 1] == ' ':
            board[position - 1] = current_player
            if check_win(current_player):
                print_board()
                print('Player', current_player, 'wins!')
                break
            if ' ' not in board:
                print_board()
                print('It\'s a tie!')
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move. Try again.')

# Start the game
play_game()
