import GAME as game
import gc as gc
import math

# SELECT VERSION (A or B)
version = 'A'

# SELECT N (game will be simulated on board sizes 1x1 to N x N)
N = 10

# SELECT IF YOU WANT TO USE ALPHA-BETA PRUNING
PRUNE = False

# SELECT CUTOFF LEVEL (if you dont want to use cutoff, use math.inf here)
CUTOFF = math.inf

game.printChart()
for i in range(1, N+1):
    gc.collect()  # clean up any allocated memory now, before we start timing stuff
    if version is 'A':
    	game.VariationA(i, PRUNE, CUTOFF)
    else:
    	game.VariationB(i, PRUNE, CUTOFF)