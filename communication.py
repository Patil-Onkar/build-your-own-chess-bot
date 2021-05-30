import sys
import chess
import argparse
from quinscence_search import quinscence_move




def talk():
    """
    The main input/output loop.
    This implements a slice of the UCI protocol.
    """
    board = chess.Board()
    #global Time
    #Time=get_time()


    while True:
        msg = input()
        print(f">>> {msg}", file=sys.stderr)
        command(board, msg)


def command(board: chess.Board, msg: str):
    """
    Accept UCI commands and respond.
    The board state is also updated.
    """
    if msg == "quit":
        sys.exit()

    if msg == "uci":
        print("ID Name : Hunter")  
        print("Auther Onkar")
        print("uciok")
        return

    if msg == "isready":
        print("readyok")
        return

    if msg == "ucinewgame":
        return

    if "position startpos moves" in msg:
        moves = msg.split(" ")[3:]
        board.clear()
        board.set_fen(chess.STARTING_FEN)
        for move in moves:
            board.push(chess.Move.from_uci(move))
        return

    if "position fen" in msg:
        fen = " ".join(msg.split(" ")[2:])
        board.set_fen(fen)
        return

    if msg[0:2] == "go":
        _move = quinscence_move(board,20)
        print(f"bestmove {_move}")
        return

def get_time():
    parser=argparse.ArgumentParser()
    parser.add_argument("--time", default=25, help="provide an time in integer (default: 25)")
    args = parser.parse_args()
    return max([10,int(args.time)])
  