# Build your own chess bot  

![](chess_gif2.gif)  



## About  

There are two kinds of chess engines as of now. One relies on search algorithms and some heuristic techniques while the other use machine learning. Stockfish and Alphazero are the two leading examples of these two kinds of engines respectively. Here, I used commonely used search algorithm alpha-beta pruning as a base. Iterative deepening and quinescene search is used on top of it to improve the search quality. Michniewski's simplified evaluation function is used to evaluate the board state. Finally the engine is hooked to lichess API.  


![image](https://user-images.githubusercontent.com/39105103/121794580-14d18b80-cc27-11eb-9f5f-23e362fd1ece.png)  


As seen from above example, any of the above three scripts can be used to build chess engine. Then generated move is converted to uci protocol and used to communicate with bot API.  


## How to use it.  

There are two major steps - 1. Create a chess engine. 2. Link it to lichess API.  

### Create a chess engine.  

    -  Convert main.py script in executable format. Or use already converted executable files from 'dist/main' (Not Recommended).  
    
    -  To make experiment with search algorithm. 'Iterative deepening','quinescene search' and 'Generate move' are three scripts to generate a chess move by three different ways. You can make chages to it or create your own. 
    
    - Run play.py script to compete between different move generation scripts. It helps to know how well the algorithm work.
    
### Link to lichess API.  

    - Download the lichess-bot-bridge from - https://github.com/ShailChoksi/lichess-bot  
    
    - Create a bot account on lichess platform. - https://lichess.org/api#operation/botAccountUpgrade  
    
    - Enter the bot credentials in configure.yml file. In lichess-bot repo 
    
    - Copy all executable files of main.py into engine folder - In lichess-bot repo  
    
    - Run lichess-bot.py  
    
    
## Future Work  

  - Use Reinforcement learning and monte-carlo tree 
 
