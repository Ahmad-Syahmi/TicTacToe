import sys

#Setting Up
Board = {
        '1' : ' ', '2' : ' ', '3' : ' ',
        '4' : ' ', '5' : ' ', '6' : ' ',
        '7' : ' ', '8' : ' ', '9' : ' '
        }

def setBoard(b):
    print(b['1'] + '|' + b['2'] + '|' + b['3'])
    print('-+-+-')
    print(b['4'] + '|' + b['5'] + '|' + b['6'])
    print('-+-+-')
    print(b['7'] + '|' + b['8'] + '|' + b['9'])

shapes = ['X','O']

class person:
    name = ''
    shape = ''
    def __init__(self):
        self.name = input('Hello, Player, What is your name? ')
        tmp = input(f'Awesome, {self.name}, choose your shape, either O or X : ')
        while tmp not in shapes:
            tmp = input(f'You made a mistake {self.name}, choose your shape, either O or X : ')
        shapes.remove(tmp)
        self.shape = tmp
        
player1 = person()
print('\n')
player2 = person()
print('\n')

print(f'Alright, {player1.name} will be Player One with the shape {player1.shape}')
print(f'Alright, {player2.name} will be Player Two with the shape {player2.shape} \n')

def positions():
    print('Here are the positions you will play in the game of Tic Tac Toe! \n')
    print('1' + '|' + '2' + '|' + '3')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('7' + '|' + '8' + '|' + '9')

positions()

print("\nLet's Start\n")

#Playing
count = 0

def game(num, board):
    place = 0
    if num % 2 == 0:
        print(f"\nIt's {player1.name}'s Turn")
        while (place < 1 or place > 9):
            place = int(input(f'Choose where you would like to place your {player1.shape} shape : '))
        board[str(place)] = player1.shape

    elif num % 2 != 0:
        print(f"It's {player2.name}'s or {player2.shape}'s Turn")
        while (place < 1 or place > 9):
            place = int(input(f'Choose where you would like to place your {player2.shape} shape : '))
        board[str(place)] = player2.shape
    return board

def win(num):
    if num % 2 == 0:
        print(f"Congrats! {player1.name} won the game :D")
        sys.exit
    elif num % 2 != 0:
        print(f"Congrats! {player2.name} won the game :D")
        sys.exit

def checkWin(num, b):
    if (b['1'] == b['2'] == b['3'] != ' '):
        win(num)
    elif (b['1'] == b['4'] == b['7'] != ' '):
        win(num)
    elif (b['7'] == b['8'] == b['9'] != ' '):
        win(num)
    elif (b['3'] == b['6'] == b['9'] != ' '):
        win(num)
    elif (b['4'] == b['5'] == b['6'] != ' '):
        win(num)
    elif (b['7'] == b['8'] == b['9'] != ' '):
        win(num)
    elif (b['1'] == b['5'] == b['9'] != ' '):
        win(num)  
    elif (b['7'] == b['5'] == b['3'] != ' '): 
        win(num) 
    elif (b['2'] == b['5'] == b['8'] != ' '):
        win(num)

for i in range(9):
    setBoard(game(count, Board))
    checkWin(count, Board)
    count += 1
    


