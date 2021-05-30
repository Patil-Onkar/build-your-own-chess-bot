'''
OPTIONAL

This is the implementation of plain minimax and plain alpha-beta algorithm for a reference

'''



import chess
from evaluate_board import final_evaluation

def next_move(b,depth=3):
    #score=-float('inf')
    alp=-float('inf')
    bet=float('inf')
    maximize=b.turn==chess.WHITE
    if maximize:
        score=-float('inf')
    else:
        score=float('inf')
    moves=list(b.legal_moves)
    best_move=moves[0]
    for move in moves:
        b.push(move)
        #value=minmax(b,depth-1,not maximize)
        value=alphabeta(b,depth-1,not maximize,alp,bet)
        #print(value)
        if maximize and value>score:
            #print(value)
            score = value
            best_move=move
        if not maximize and value<score:
            #print(value)
            score=value
            best_move=move
        b.pop()
    #print(best_move)
    return best_move

def minmax(b,d,maximize):
    if b.is_checkmate():
        return -float('inf') if maximize else float('inf')
    if b.can_claim_draw():
        return 0.0
    if d==0:
        return final_evaluation(b)
    moves=list(b.legal_moves)
    if maximize:
        score = -float('inf')
        for move in moves:
            b.push(move)
            value=minmax(b,d-1,not maximize)
            if value>score:
                score=value
            b.pop()
        return score
    else:
        score=float('inf')
        for move in moves:
            b.push(move)
            value = minmax(b, d - 1, not maximize)
            if value<score:
                score=value
            b.pop()
        return score




def alphabeta(b,d,maximize,alp,bet):
    if b.is_checkmate():
        return -float('inf') if maximize else float('inf')
    if b.can_claim_draw():
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

