# Build your own chess bot  

## About  

There are two kinds of chess engines as of now. One relies on search algorithms and some heuristic techniques while the other use machine learning. Stockfish and Alphazero are the two leading examples of these two kinds of engines respectively. Here, I used commonely used search algorithm alpha-beta pruning as a base. Iterative deepening and quinescene search is used on top of it to improve the search quality. Michniewski's simplified evaluation function is used to evaluate the board state. Finally the engine is hooked to lichess API   .
 
