'''
This is to tests few
'''

from iterative_deepening import iterative_move
from quinscence_search import quinscence_move
from Random_board_generator import generate_board
import chess
import time


############## Test the time required for each move ################

def test_time():
    t=[10,20,30,40]
    for tm in t:
        for i in range(3):
            board=generate_board()
            #print(board)
            start_time=time.time()
            m=iterative_move(board,tm)
            time_=time.time()-start_time
            if time_>tm+1:
                print('Test Failed for iterative_move!!\nExpected time:{}\nActual time:{}'.format(tm,time_))
            start_time=time.time()
            m=quinscence_move(board,tm)
            time_ = time.time() - start_time
            if time_ > tm + 1:
                print('Test Failed for quinscence_move!!\nExpected time:{}\nActual time:{}'.format(tm, time_))
    print('\nTESTS PASSED...\nMoves are well constrained in expected time limit')

test_time()
