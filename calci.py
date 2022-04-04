
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

test_board=['#','O','X','X','O','X','O','X','X','O']
# display_board(test_board)

def player_input():
    # '''
    # output=(player 1 marker,player 2 marker)
    # '''

    marker=' '
    while marker!='X' and marker!='O':
        marker=input('player1: chose X or O').upper()

    if marker=='X':
        return('X','O')
    else:
        return('O','X')
# player_input()


def place_marker(board,marker,position):
    board[position] = marker



place_marker(test_board,'$',7)
# place_marker(test_board,'O',2)
# display_board(test_board)

def win_check(board,mark):
    return ((board[7]==board[8]==board[9]==mark)or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))





import random

def choose_first():
    flip=random.randint(0,1)

    if flip==0:
        return 'player 1'
    else:
        return 'player 2'


def space_check(board,position):
    return board[position]==' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False #board is not full
    #board is full
    return True


def player_choice(board):
    position= 0

    while position not in range(0,10) or not space_check(board, position):
        position=int(input('choose a position:(1-9)'))
    return position


def replay():
    input('Play again ? enter Yes or No')
    return choice=='Yes'



print('Welome to tic tac toe')

while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn + ' will go first')

    play_game=input('ready to play? y or n?')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player 1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    game_on=False
                else:
                    turn='player 2'


        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    game_on = False
                else:
                    turn = 'player 1'



        if not replay():
            break





































