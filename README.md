# N-Queens-Game

Written in Python 3

The N-Queens problem is to put N Queens on a board (N × N ) so that no queen attacks any other queen. (A queen can attack any square on the same row, same column, or same diagonal.) This project is a two player game of the N-queens problem. Used to explore the AI technologies in a two player, deterministic, perfect information, zero sum environment. It will show the use of the MiniMax algorithm, the benefits of Alpha-Beta pruning, and also how a depth-cutoff and heuristic evaluation function for MiniMax search can improve execution time to allow for larger NxN game boards.

The game board is a standard NxN chess board.
Players will alternate playing a queen on the board. The players must place a queen in the left-most unoccupied column, and a queen can only be placed in a square that is not being attacked. An attack is a standard chess queen attack, i.e there is no queen already on the board in the same row, column or diagonal. The winner of the game is the last player to have a legal place to put a queen. The way the game is implemented currently, is two AI players play against each other. Provided will be scripts to play different 

There are two possible variations implemented for this game differing in how score is counted

Version A : The game will return 1 for a Player 1 win, and a -1 for a Player 2 win. Player 1 will always play the first move.

Version B : The score will be counted by counting how many queens are on the board at the end of the game. if there are k queens on the board and it is a win for player 1, the score is k, if it is a win for player 2, the score is -k. 


The application can be used in 2 ways.

1. You can use the application to analyze the impact of different algorithms on this problem.
Execution will run a simulation on board sizes 1x1 to NxN. It will then print a data able showing the results for each simulation, who won, what was the best opening move(X=player1), and what was the execution time. This allows data analysis of the effect of the above technologies, and how changing the game settings can impact performance.

Settings can be changed on lines 5-7 in GameAnalysis.py

Execution instructions:

  1. Download all files
  2. Navigate to the directory
  3. Execute the desired file.
     Sample execution: python3 GameAnalysis.py 
     with settings:
        version = 'A'
        N = 20
        PRUNE = False
        CUTOFF = 4
     
     will produce the below chart 
     
SAMPLE OUTPUT 
###############################################################

Size   Minimax Value   Best Opening Move   Time in Seconds
___________________________________________________________
  1         1            ('X', 0)         0.00003004
  2         1            ('X', 0)         0.00018287
  3         1            ('X', 1)         0.00008607
  4        -1            ('X', 0)         0.00024605
  5       0.0625         ('X', 4)         0.00101590
  6      -0.5318         ('X', 1)         0.00290298
  7      -0.4414         ('X', 2)         0.01057196
  8      -0.2848         ('X', 0)         0.02664495
  9      -0.2051         ('X', 5)         0.04405618
 10      -0.3911         ('X', 9)         0.08285213
 11      -0.3255         ('X', 8)         0.14697123
 12      -0.4115         ('X', 0)         0.26428890
 13      -0.4975         ('X', 7)         0.45815873
 14      -0.5772         ('X', 0)         0.70609808
 15      -0.5366         ('X', 14)        1.07694817
 16      -0.6284         ('X', 2)         1.63673711
 17      -0.6486         ('X', 15)        2.48325515
 18      -0.6556         ('X', 1)         3.74760604
 19      -0.6803         ('X', 12)        5.30632091
 20      -0.6921         ('X', 0)         8.91690588

############################################################### 


2. You can use the application to run a simulation of an interactive game between 2 AI players.
Execution will run the selected amount of simulations on board size NxN. It will then print a data able showing the results for each round , value of N, cutoff level for each player, and win/loss ratio for player 1. This allows data analysis of the effect of the above technologies, and how changing the game settings can impact performance.

Settings can be changed on lines 5-19 in InteractiveGameAnalysis.py

Execution instructions:

  1. Download all files
  2. Navigate to the directory
  3. Execute the desired file.
     Sample execution: python3 InteractiveGameAnalysis.py 
     with settings:
       Version = "A"
       p1_cutoff = 3
       p2_cutoff = 5
       N = 20
       best_of = 5
       p1_prune = True
       p2_prune = True
     
     will produce the below chart 
###############################################################

N  Cutoff P1   Cutoff P2   win/loss P1
___________________________________________________________
20     3          5          11 W, 9 L
20     3          5          12 W, 8 L
20     3          5          13 W, 7 L
20     3          5          7 W, 13 L
20     3          5          12 W, 8 L

###############################################################

Thank you for viewing my application.
