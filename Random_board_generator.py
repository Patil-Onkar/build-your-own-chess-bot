'''
It generates random board state
'''

import chess
import random
def generate_board():
    n=random.randint(8,20)
    board=chess.Board()
    for i in range(n):
        m=random.choice(list(board.legal_moves))
        board.push(m)
    return board
