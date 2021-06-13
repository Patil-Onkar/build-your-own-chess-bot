import chess
from Generate_move import next_move
from iterative_deepening import iterative_move
from quinscence_search import quinscence_move
from evaluate_board import final_evaluation
#from Random_board_generator import start
import random

import time
from IPython.display import display, HTML, clear_output


def player1(board):
    m=quinscence_move(board,20)
    return m
def player2(board):
    m=iterative_move(board,20)
    return m
def player3(board):
    if len(list(board.legal_moves))==0:
        print(board)
        print(board.fen())
    m=random.choice(list(board.legal_moves))
    return m

def no_of_matches(n):
    for i in range(n):
        board=chess.Board()
        pl1=False
        if random.choice([True,False]):
            m=player1(board)
            board.push(m)
            print('We got White')
            pl1=True
        while not (board.can_claim_draw() or board.is_checkmate()):
            m=player2(board)
            if board.is_capture(m):
                board.push(m)
                print(board,'\n')
                board.pop()
            board.push(m)
            if board.can_claim_draw() or board.is_stalemate():
                print('\n\nDraw\n\n')
                break
            if board.is_checkmate():
                if not pl1==board.turn:
                    print('\n\nWin\n\n')
                else:
                    print('Loose',end=' ')
                break
            m=player1(board)
            if board.is_capture(m):
                board.push(m)
                print(board,'\n')
                board.pop()
            board.push(m)
            if board.can_claim_draw() or board.is_stalemate():
                print('Draw',end=' ')
                break
            if board.is_checkmate():
                if not pl1==board.turn:
                    print('Win',end=' ')
                else:
                    print('Loose',end=' ')
                break





#Begin


no_of_matches(5)




