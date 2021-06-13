# Build your own chess bot  

## About  

There are two kinds of chess engines as of now. One relies on search algorithms and some heuristic techniques while the other use machine learning. Stockfish and Alphazero are the two leading examples of these two kinds of engines respectively. Here, I used commonely used search algorithm alpha-beta pruning as a base. Iterative deepening and quinescene search is used on top of it to improve the search quality. Michniewski's simplified evaluation function is used to evaluate the board state. Finally the engine is hooked to lichess API.  


![image](https://user-images.githubusercontent.com/39105103/121794580-14d18b80-cc27-11eb-9f5f-23e362fd1ece.png)  


As seen from above example, any of the above three scripts can be used to build chess engine. Then generated move is converted to uci protocol and used to communicate with bot API.  


## How to use it.  

There are two major steps - 1. Create a chess engine. 2. Link it to lichess API.  

### Create a chess engine.  

    -  Convert main.py script in executable format. Or use already converted executable files from 'dist/main' (Not Recommended).  
    
    -  To make experiment with search algorithm. 'Iterative deepening','quinescene search' and 'Generate move' are three scripts to generate a chess move. You can make chages to it or create your own. And to check the improvement, use play.py script that will allow you to fight among your bots.
    
    - Link the 
 
