import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Call the function to print the board
display_board(board)

def check_win(board, mark):
    if (
            board[0] == board[1] == board[2] == mark
            or board[3] == board[4] == board[5] == mark
            or board[6] == board[7] == board[8] == mark
            or board[0] == board[3] == board[6] == mark
            or board[1] == board[4] == board[7] == mark
            or board[2] == board[5] == board[8] == mark
            or board[0] == board[4] == board[8] == mark
            or board[2] == board[4] == board[6] == mark
    ):
        return True

    return False

def check_draw(board):
    return all(space in ["X", "O"] for space in board)


while True:
    while True:
        # ask Player X for a position
        player_x = int(input("Player X please enter a number between 1 and 9:\n"))
        player_x -= 1
        print(f"you have made the player:  {player_x + 1}")
        print("---------------------")


        if board[player_x] in ["X", "O"]:
            print("The position is taken")
        else:
            board[player_x] = "X"
            display_board(board)
            break

    if check_win(board, "X"):
        print("Player X wins!")
        break

    if check_draw(board):
        print("Its a draw!")
        break


    while True:
        # ask Player O for a position
        player_o = int(input("Player O please enter a number between 1 and 9:\n"))
        player_o -= 1
        print(f"you have made the player:  {player_o + 1}")
        print("---------------------")

        if board[player_o] in ["X", "O"]:
            print("The position is taken")
        else:
            board[player_o] = "O"
            display_board(board)
            break

    if check_win(board, "O"):
        print("Player O wins!")
        break

    if check_draw(board):
        print("Its a draw!")
        break

