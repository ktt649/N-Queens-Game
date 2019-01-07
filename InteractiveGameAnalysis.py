import INTERACTIVE_GAME as IGame

# SELECT VERSION (A or B)
Version = "A"

# SELECT CUTOFF LEVEL (if cutoff > N then there is no cutoff)
p1_cutoff = 3
p2_cutoff = 5

# SELECT N (game will be simulated N x N board)
N = 20

# SELECT HOW MANY GAMES YOU WANT TO SIMULATE
best_of = 5

# SELECT IF YOU WANT TO USE ALPHA-BETA PRUNING
p1_prune = True
p2_prune = True

IGame.play_game(Version, p1_cutoff, p2_cutoff, N, best_of, p1_prune, p2_prune)