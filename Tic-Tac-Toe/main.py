import random


def display_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True

    return False


def play_rps():
    choices = ['rock', 'paper', 'scissors']
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
        return 'tie'
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win!")
        return 'win'
    else:
        print("You lose!")
        return 'lose'


def erase_piece(board):
    while True:
        position = int(input("Enter the position (1-9) of the piece you want to erase: ")) - 1
        if board[position] != ' ':
            board[position] = ' '
            break
        else:
            print("Invalid position. Please choose a non-empty position.")


def play_game():
    board = [' '] * 9
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        display_board(board)

        if check_win(board):
            print("Player", current_player, "wins!")
            break

        if ' ' not in board:
            print("It's a tie!")
            break

        if input("Do you want to challenge your opponent to a game of Rock-Paper-Scissors? (y/n): ").lower() == 'y':
            result = play_rps()

            if result == 'win':
                erase_piece(board)
            elif result == 'lose':
                current_player = players[(players.index(current_player) + 1) % 2]

        position = int(input("Player " + current_player + ", enter your move (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player
            current_player = players[(players.index(current_player) + 1) % 2]
        else:
            print("Invalid move. Please choose an empty position.")

play_game()