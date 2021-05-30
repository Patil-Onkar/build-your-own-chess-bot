import chess
import argparse
from Generate_move import next_move
from iterative_deepening import iterative_move
from quinscence_search import quinscence_move
import random

def random_gen(board):
    m = random.choice(list(board.legal_moves))
    return m

def start():
    """
    Start the command line user interface.
    """
    d={'i':iterative_move,'q':quinscence_move,'r':random_gen,'y':get_move}
    while True:
        player1=input('Enter player 1 from {[i]terative_deepening,[q]uinscence_search,[r]andom_move_generator or [y]ou}')
        player2=input('Enter player 2 from {[i]terative_deepening,[q]uinscence_search,[r]andom_move_generator or [y]ou}')
        if player1 in d.keys() and player2 in d.keys():
            break
        else:
            print('please enter players in correct format')

    board=chess.Board()
    chck=False
    if random.choice([True,False]):
        chck=True
        print('Lets begin!!\n\nplayer 1 will take white\n')
        print(render(board))
        board.push(d[player1](board))
        print(render(board))
    if not chck:
        print('Lets begin!!\n\nplayer 2 will take white\n')
        print(render(board))
    while True:
        m=d[player2](board)
        board.push(m)
        print(render(board))
        if board.can_claim_draw() or board.is_stalemate():
            print('\n\nDraw\n\n')
            break
        if board.is_checkmate():
            if not chck == board.turn:
                print('\n\nPlayer 1 WON\n\n')
            else:
                print('\n\nPlayer 2 WON\n')
            break
        m = d[player1](board)
        board.push(m)
        print(render(board))
        if board.can_claim_draw() or board.is_stalemate():
            print('Draw', end=' ')
            break
        if board.is_checkmate():
            if not chck == board.turn:
                print('\n\nPlayer 1 WON\n')
            else:
                print('\n\nPlayer 2 WON\n')
            break





def render(board: chess.Board) -> str:
    """
    Print a side-relative chess board with special chess characters.
    """
    board_string = list(str(board))
    uni_pieces = {
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "P": "♙",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "p": "♟",
        ".": "·",
    }
    for idx, char in enumerate(board_string):
        if char in uni_pieces:
            board_string[idx] = uni_pieces[char]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []
    for rank in "".join(board_string).split("\n"):
        display.append(f"  {ranks.pop()} {rank}")
    #if board.turn == chess.BLACK:
    #    display.reverse()
    display.append("    a b c d e f g h")
    return "\n" + "\n".join(display)

def get_move(board: chess.Board) -> chess.Move:
    """
    Try (and keep trying) to get a legal next move from the user.
    Play the move by mutating the game board.
    """
    move = input(f"\nYour move (e.g. {list(board.legal_moves)[0]}):\n")

    for legal_move in board.legal_moves:
        if move == str(legal_move):
            return legal_move
    return get_move(board)

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        pass
