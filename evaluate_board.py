'''
Here chess-board is evaluated.

For each piece on the board, its position value and piece value is calculated.
As per Tomasz Michniewski's  Simplified Evaluation Function,

'''

import chess



# points to each piece
piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

#Give position weightage to each square for each piece
pawnEvalWhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5, 5, 10, 25, 25, 10, 5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    5, 10, 10, -20, -20, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0,
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0,
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20,
]

kingEvalWhite = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20,
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))



# Order the available moves,
#to increase speed of alpha-beta search

def move_value(move,board,isendgame):
    '''
    It evaluate a move based on ots position change and capture

    :param move: chess-move
    :param board: chess-board
    :param isendgame: Is board at the end state
    :return: score of the move
    '''

    maximize=board.turn==chess.WHITE
    if move.promotion:
        value=float('inf') if maximize else -float('inf')
    capture=0.0
    if board.is_capture(move) and not board.is_en_passant(move):
        p1=piece_value[board.piece_at(move.from_square).piece_type]
        p2=piece_value[board.piece_at(move.to_square).piece_type]
        if p1<p2:
            capture=p2+(p2-p1)/2
        else:
            capture=p2
    pos_value=position_score(board.piece_at(move.from_square),move.to_square,isendgame)-position_score(board.piece_at(move.from_square),move.from_square,isendgame)
    total_value=capture+pos_value
    if maximize:
        return total_value
    else:
        return -total_value

def move_order(board):
    '''
    based on each move value this function arrange all the legal moves in descending order

    :param board: Chess-Board
    :return: All the moves in order
    '''

    isendgame=endgame(board)
    def order(move):
        return move_value(move,board,isendgame)
    moves=sorted(board.legal_moves,key=order,reverse=board.turn==chess.WHITE)
    return list(moves)

# Checking the game state

#As per michniwiki if there are 2 queens and 1 minor or no queens then we are in endgame
# following function checks the endgame condition
def endgame(board):
    '''
    It checks if we are in end-game or not

    :param board: Chess-board
    :return: Boolean value, True or False
    '''

    queens=0
    minors=0
    for sq in chess.SQUARES:
        ps=board.piece_at(sq)
        if ps and ps.piece_type==chess.QUEEN:
            queens+=1
        if ps and (ps.piece_type==chess.BISHOP or ps.piece_type==chess.KNIGHT):
            minors+=1
    #print(queens,minors)
    if queens==0 or (queens==2 and minors<=1):
        return True
    else :
        return False


def position_score(p,square,isendgame):
    '''
    It calculates position score for a particular piece

    :param p: Piece-type
    :param square: square where piece lies
    :param isendgame: Bool value, Are we in endgame
    :return: Positional scores
    '''

    piece=p.piece_type
    if piece==chess.PAWN:
        #print('a')
        lst=pawnEvalWhite if chess.WHITE==p.color else pawnEvalBlack
    if piece==chess.ROOK:
        #print('b')
        lst=rookEvalWhite if chess.WHITE==p.color else rookEvalBlack
    if piece==chess.BISHOP:
        #print('c')
        lst= bishopEvalBlack if chess.WHITE==p.color else bishopEvalBlack
    if piece==chess.QUEEN:
        #print('d')
        lst= queenEval
    if piece==chess.KNIGHT:
        #print('e')
        lst=knightEval
    if isendgame:
        #print('f')
        if piece==chess.KING:
            #print('g')
            lst=kingEvalEndGameWhite if chess.WHITE==p.color else kingEvalEndGameBlack
    else:
        #print('h')
        if piece==chess.KING:
            #print('i')
            lst=kingEvalWhite if chess.WHITE==p.color else kingEvalBlack

    return lst[square]


def final_evaluation(board):

    '''
    It sums up both positional score and piece values, for all the pieces on board

    :param board: chess-board
    :return: Final evaluation score of board
    '''

    total=0
    isendgame=endgame(board)
    for sq in chess.SQUARES:
        p=board.piece_at(sq)
        if bool(p):
            value=position_score(p,sq,isendgame)+piece_value[p.piece_type]
            if p.color==chess.WHITE:
                total=total+value
            else:
                total=total-value
    return total

