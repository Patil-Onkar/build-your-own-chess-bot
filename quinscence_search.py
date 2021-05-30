'''
Implementation of quinscence search along with iterative deepening and alpha-beta pruning
'''


import chess
from evaluate_board import final_evaluation,piece_value
import time
from evaluate_board import move_order

#global variables
Quin_depth=20

def quinscence_move(board,t=20):
    '''
    Calculate next bestmove

    :param board: chess-board variable (current board state)
    :param t: (Time limit for one move)
    :return: chess move
    '''

    if board.ply()<2:
        return first_move(board)
    global Time
    global start_time
    start_time=time.time()
    Time=t
    depth=2
    moves = move_order(board)
    best_move = moves[0]
    while True:
        global_best_move=best_move
        alp=-float('inf')
        bet=float('inf')
        maximize=board.turn==chess.WHITE
        if maximize:
            score=-float('inf')
        else:
            score=float('inf')
        for move in moves:
            board.push(move)
            value=alphabeta(board,depth-1,not maximize,alp,bet)
            if maximize and value>score:
                score = value
                best_move=move
            if not maximize and value<score:
                score=value
                best_move=move
            board.pop()
        if time.time()-start_time>=Time:
            break
        depth += 1
    return global_best_move



def alphabeta(board,depth,maximize,alp,bet):
    '''
    Implementation of Alpha-Beta algorithm

    :param board: chess-board variable (current state of board)
    :param depth: Depth to be explored
    :param maximize: Boolean value(True or False); used to check whether to minimize or maximize
    :param alp: Alpha constant
    :param bet: Beta Constant (both alpha and beta constants are used to cut off the unnecessary branches)
    :return: maximum/minimum node value
    '''
    if time.time()-start_time>=Time:
        return 0.0
    if board.is_checkmate():
        return -float('inf') if maximize else float('inf')
    if board.can_claim_draw() or board.is_stalemate():
        return 0.0
    if depth==0:
        return quinscence_search(board,1,maximize,alp,bet)
    moves= move_order(board)
    if maximize:
        score = -float('inf')
        for move in moves:
            board.push(move)
            score=max(alphabeta(board,depth-1,not maximize,alp,bet),score)
            alp=max(score,alp)
            board.pop()
            if alp>bet:
                break
        return score
    else:
        score=float('inf')
        for move in moves:
            board.push(move)
            score=min(alphabeta(board,depth-1,not maximize,alp,bet),score)
            bet=min(score,bet)
            board.pop()
            if bet<alp:
                break
        return score


def quinscence_search(board,depth,maximize,alp,bet):
    '''
    it is used to do quinscence search at unstable node

    :param board: chess-board variable (current state of board)
    :param depth: Depth to be explored
    :param maximize: Boolean value(True or False); used to check whether to minimize or maximize
    :param alp: Alpha constant
    :param bet: Beta Constant (both alpha and beta constants are used to cut off the unnecessary branches)
    :return: maximum/minimum node value
    '''
    moves=[]
    for move in board.legal_moves:
        if favourable(board,move):
            moves.append(move)
    if depth>=Quin_depth or len(moves)==0:
        return final_evaluation(board)
    if maximize:
        score=alp
        for move in moves:
            board.push(move)
            move_score=quinscence_search(board,depth+1,not maximize,alp,bet)
            board.pop()
            if move_score>score:
                score=move_score
                if score>bet:
                    break
        return score
    else:
        score=bet
        for move in moves:
            board.push(move)
            move_score=quinscence_search(board,depth+1,not maximize,alp,bet)
            board.pop()
            if move_score<score:
                score=move_score
                if score<alp:
                    break
        return score



def favourable(board,move):
    '''
    This function checks, if given move is favourable or not

    :param board: chess-board variable (current state of board)
    :param move: chess move
    :return: Bool (favourable or not)
    '''
    if move.promotion is not None:
        return True
    if board.is_capture(move) and not board.is_en_passant(move):
        if piece_value[board.piece_type_at(move.from_square)] < piece_value[board.piece_type_at(move.to_square)] or len(board.attackers(board.turn,move.to_square))>len(board.attackers(not board.turn,move.to_square)):
            return True
    return False


def first_move(board):
    '''
    This is to hardcode first move
    :param board: chess-board variable (current state of board)
    :return: first chess move
    '''
    if board.turn==chess.WHITE:
        return chess.Move.from_uci('e2e4')
    else:
        return chess.Move.from_uci('g8f6')




#b=chess.Board()
#quinscence_move(b,300)


