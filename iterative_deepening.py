'''
This is implementation of iterative deepening algorithm on the top of alpha-beta pruning.
time parameter is added to cut-off the searching process when its time's up.
'''


import chess
from evaluate_board import final_evaluation
import time


def iterative_move(b,t=20):
    '''
    :param b: it is the chess-board variable (current state of board)
    :param t: Time limit for one move
    :return: chess move
    '''
    global Time
    global start_time
    start_time=time.time()
    Time=t
    depth=2
    moves = list(b.legal_moves)
    best_move = moves[0]
    while True:
        global_best_move=best_move
        alp=-float('inf')
        bet=float('inf')
        maximize=b.turn==chess.WHITE
        if maximize:
            score=-float('inf')
        else:
            score=float('inf')
        for move in moves:
            b.push(move)
            value=alphabeta(b,depth-1,not maximize,alp,bet)
            if maximize and value>score:
                score = value
                best_move=move
            if not maximize and value<score:
                score=value
                best_move=move
            b.pop()
        if time.time()-start_time>=Time:
            break
        depth += 1
    return global_best_move



def alphabeta(b,d,maximize,alp,bet):
    '''
    :param b: it is the chess-board variable (current state of board)
    :param d: Depth to be explored
    :param maximize: Boolean value(True or False); used to check whether to minimize or maximize
    :param alp: Alpha constant
    :param bet: Beta Constant (both alpha and beta constants are used to cut off the unnecessary branches)
    :return: maximum/minimum node value
    '''
    if time.time()-start_time>=Time:
        return 0.0
    if b.is_checkmate():
        return -float('inf') if maximize else float('inf')
    if b.can_claim_draw() or b.is_stalemate():
        return 0.0
    if d==0:
        return final_evaluation(b)
    moves=list(b.legal_moves)
    if maximize:
        score = -float('inf')
        for move in moves:
            b.push(move)
            score=max(alphabeta(b,d-1,not maximize,alp,bet),score)
            alp=max(score,alp)
            b.pop()
            if alp>bet:
                break
        return score
    else:
        score=float('inf')
        for move in moves:
            b.push(move)
            score=min(alphabeta(b,d-1,not maximize,alp,bet),score)
            bet=min(score,bet)
            b.pop()
            if bet<alp:
                break
        return score


#b=chess.Board()
#iterative_move(b,60)