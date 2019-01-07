import GAME as vA

#Prints the heading of the data table for interactive n-queens game
def printTable():
    print()
    print("N  Cutoff P1   Cutoff P2   win/loss P1")
    print("___________________________________________________________")

#Prints data for the data table for interactive n-queens game
def printData(n, p1, p2, win, loss):
    print(n,"   ", p1, "        ", p2, "        ", win,"W,", loss,"L")

'''
Plays two AI players against each other in the interactive n-queens game
version: variation of N queens
p1cut: search cutoff for p1
p2cut: search cutoff for p2
N: game will be played for board size 1-N
bestof: how many iterations you want to play (example, best of 5)
p1_prune: True if player 1 should use Alpha-Beta pruning
p2_prune: True if player 2 should use Alpha-Beta pruning
'''
def play_game(version, p1cut, p2cut, N, bestof, p1_prune, p2_prune):
    printTable()

    for rounds in range(bestof):
        p1W = 0
        p1L = 0
        for gameSize in range(1, N+1):
            GAME_OVER = False
            board = []
            if version == "A":
                p1game = vA.VariationA(gameSize, p1_prune, p1cut, True, board)
            else:
                p1game = vA.VariationB(gameSize, p1_prune, p1cut, True, board)

            if version == "A":
                p2game = vA.VariationA(gameSize, p2_prune, p2cut, True, board)
            else:
                p2game = vA.VariationB(gameSize, p2_prune, p2cut, True, board)

            turns = gameSize
            while turns >= 0 and not GAME_OVER:
                # Player 1's turn
                if not GAME_OVER:
                    player1 = p1game.playMove(p1cut)

                    if player1 == None:
                      #  print("GAME OVER Player 2 wins!")
                        GAME_OVER = True
                        p1L +=1
                    turns = turns - 1

                #Player 2's turn
                if not GAME_OVER:
                    player2 = p2game.playMove(p2cut)

                    if player2 == None:
                      #  print("GAME OVER Player 1 wins!")
                        GAME_OVER = True
                        p1W += 1
                    turns = turns - 1

        printData(N, p1cut, p2cut, p1W, p1L)

