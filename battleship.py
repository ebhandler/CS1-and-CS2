'''
Name: Evelyn Handler
Date: 4/9/26
Description: Battleship game 
'''

import time
import os

def create_board(board):
    print (f'''  1    2    3    4    5
1  {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} 
  -------------------------
2  {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]}  
  -------------------------
3  {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} 
  -------------------------
4  {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} 
  -------------------------
5  {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} 
    ''') 
    

def place_ship(board, name):
    '''
    Asks the player for a row and column
    Args:
        Board: (list) game board
        Player: (str) Player2, what is your name or Player1, what is your name
    Returns:
        None
    '''
    while True:
        row = int(input(f"{name}, which row do you pick?  🤔⚠️🧐🤫: ")) - 1
        column = int(input(f"{name}, which column do you pick? 🤔⚠️🧐🤫: ")) - 1

        if row < 0 or row > 4 or column < 0 or column > 4 or board[row][column] != '🌊':
            print('Space not available')
            continue
        break
    board[row][column] = "🚢"
    create_board(board)


def shooting_cordinates(board, shooting_board, name, counter):
    '''
    Shoots at the other players board
    Args:
        Board (list): the other players board 
        Shooting board (list): the board displaying hits and misses 
    Returns:
        None: Updates shooting board with either hits or misses
    '''
    create_board(shooting_board)

    while True:
        row = int(input(f"{name}, which row do you pick?  🤔⚠️🧐🤫: ")) - 1
        column = int(input(f"{name}, which column do you pick? 🤔⚠️🧐🤫: ")) - 1

        if row < 0 or row > 4 or column < 0 or column > 4 or shooting_board[row][column] != '🌊':
            print('Cannot shoot that space')
            continue
        break
    if board[row][column] == '🚢':
        shooting_board[row][column] = '🔥'
        counter += 1
    else:
        shooting_board[row][column] = '😂'
    create_board(shooting_board)
    return counter

def main():
    '''
    Main loop where battleship runs 
    '''
    while True:
        p1_board = [['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊']]
        p1_shooting_board = [['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊']]
        p2_board = [['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊']]
        p2_shooting_board = [['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊'], ['🌊', '🌊', '🌊', '🌊', '🌊']]

        p1_name = input('Player1, what is your name?: ').upper()
        p2_name = input('Player2, what is your name?: ').upper()

        create_board(p1_board)

        for i in range(4):
            place_ship(p1_board, p1_name)

        time.sleep(2)
        os.system('cls')
        
        create_board(p2_board)

        for i in range(4):
            place_ship(p2_board, p2_name)

        time.sleep(2)
        os.system('cls')

        p1_counter = 0
        p2_counter = 0

        while p1_counter < 4 and p2_counter < 4:
            p1_counter = shooting_cordinates(p2_board, p2_shooting_board, p1_name, p1_counter)

            if p1_counter == 4:
                print(f'{p1_name} wins!')
                break
            p2_counter = shooting_cordinates(p1_board, p1_shooting_board, p2_name, p2_counter)

            if p2_counter == 4:
                print(f'{p2_name} wins!')
                break

main()