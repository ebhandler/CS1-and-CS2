'''
Name: Evelyn Handler
Date: 4/9/26
Description: TicTacToe game 
'''
def create_board(board):
    print (f'''  1    2   3
1  {board[0][0]} | {board[0][1]} | {board[0][2]} 
  -----------
2  {board[1][0]} | {board[1][1]} | {board[1][2]} 
  -----------
3  {board[2][0]} | {board[2][1]} | {board[2][2]} 
''') 
    
def get_player_move(board, player):
    '''
    Asks the player for a row and column
    Args:
        Board: (list) game board
        Player: (str) 'X' or 'O'
    Returns:
        None
    '''
    row = int(input("which row do you pick?  ≽^•⩊•^≼ ₊˚⊹♡: "))
    column = int(input("which column do you pick? ≽^•⩊•^≼ ₊˚⊹♡: "))
    board[row-1][column-1] = player

def check_winner(board, player):
    '''
    Checks for winning combinations 
    Args:
        None
    Returns:
        Bool: True if player wins, false if player does not win
    '''
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(f"{player} wins") 
        return True
    elif board[0][0] == player and board[0][1] == player and board[0][2] == player:
        print(f"{player} wins")
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        print(f"{player} wins")
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f"{player} wins")
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        print(f"{player} wins")
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print(f"{player} wins")
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        print(f"{player} wins")
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        print(f"{player} wins")
        return True
    else:
        return False

def is_draw(board):
    '''
    Checks for blank spots in the board
    Args:
        Board: (list) current board
    Returns:
        Bool: True if draw, false if not draw
    '''
    if board[0][0] == " " or  board[0][1] == " " or board[0][2] == " " or board[1][0] == " " or board[1][1] == " " or board[1][2] == " " or board[2][0] == " " or board[2][1] == " " or board[2][2] == " ":
        return False
    else:
        return True

def play_again():
    '''
    Asks if the player wants to play again
    Args:
        None
    Returns:
        Bool: True if player wants to play again, false if player does not want to play again
    '''
    play = input("Want to play again? Pick 'yes' or 'no'")
    if play == ("yes"):
        return True 
    elif play == ("no"):
        return False

def main():
    while True:
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        player1 = input('X or O? ').upper()

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

        while True:
            get_player_move(board, player1)
            create_board(board)
            if check_winner(board, player1):
                break
            if is_draw(board):
                print('Tie')
                break
            get_player_move(board, player2)
            create_board(board)

            if check_winner(board, player2):
                break

        if not play_again():
            break

main()