#ALPHA-BETA PRUINING MINIMAX FILE

''' ALPHA-BETA PRUNING ALGORITHM FUNCTIONS'''

'''
Returns: best value for player 1 (max) using alpha-beta pruning 
variation: the n-queens game variation that you want to use
state: a n-queens game state
maxs_best: the highest minimax value so far (best move for player 1)
mins_best: the lowest minimax value so far (best move for player 2)
'''
def max_value(variation, state, maxs_best, mins_best):
    if variation.is_terminal(state):
        best_for_max_here = variation.utility(state)
    else:
        # If at cutoff limit, estimate utility
        if variation.cutoff_test(state, variation.getLimit()):
            best_for_max_here = variation.eval(state)
        else:
            best_for_max_here = variation._negInf
            actions = variation.actions(state)

            for act in actions:
                res = variation.result(state, act)
                val = min_value(variation, res, maxs_best, mins_best)
                if val > best_for_max_here:
                    best_for_max_here = val

                if best_for_max_here >= mins_best:
                    return best_for_max_here

                maxs_best = max(maxs_best, best_for_max_here)

    return best_for_max_here

'''
Returns: best value for player 2 (min) using alpha-beta pruning
variation: the n-queens game variation that you want to use
state: a n-queens game state
maxs_best: the highest minimax value so far (best move for player 1)
mins_best: the lowest minimax value so far (best move for player 2)
'''
def min_value(variation, state, maxs_best, mins_best):
    if variation.is_terminal(state):
        best_for_min_here = variation.utility(state)
    else:
        # If at cutoff limit, estimate utility
        if variation.cutoff_test(state, variation.getLimit()):
            best_for_min_here = variation.eval(state)
        else:
            best_for_min_here = variation._posInf
            actions = variation.actions(state)

            for act in actions:
                res = variation.result(state, act)
                val = max_value(variation, res, maxs_best, mins_best)
                if val < best_for_min_here:
                    best_for_min_here = val

                if best_for_min_here <= maxs_best:
                    return best_for_min_here

                mins_best = min(mins_best, best_for_min_here)

    return best_for_min_here

'''
Implements MiniMax algorithm using alpha-beta pruning to improve performance.
Assumes is player 1's turn (max)
Returns: a tuple (minimax, bestMove)
variation: the n-queens game variation that you want to use
state: a n-queens game state
'''
def max_decision(variation, state):
    maxs_best = variation._negInf
    mins_best = variation._posInf

    actions = variation.actions(state)
    best_for_max_here = variation._negInf
    best_action = None

    for act in actions:
        res = variation.result(state, act)
        val = min_value(variation, res, maxs_best, mins_best)

        if val > best_for_max_here:
            best_for_max_here = val
            best_action = act

        maxs_best = max(maxs_best, best_for_max_here)

    return best_for_max_here, best_action

'''
Implements MiniMax algorithm using alpha-beta pruning to improve performance.
Assumes is player 2's turn (min)
Returns: a tuple (minimax, bestMove)
variation: the n-queens game variation that you want to use
state: a n-queens game state
'''
def min_decision(variation, state):
    maxs_best = variation._negInf
    mins_best = variation._posInf

    actions = variation.actions(state)
    best_for_min_here = variation._posInf
    best_action = None

    for act in actions:
        res = variation.result(state, act)
        val = min_value(variation, res, maxs_best, mins_best)

        if val < best_for_min_here:
            best_for_min_here = val
            best_action = act

        mins_best = min(mins_best, best_for_min_here)

    return best_for_min_here, best_action

'''
Uses the alpha-beta pruning algorithms to make the best decision depending on if it is player 1 or player 2s turn
variation: the n-queens game variation that you want to use
state: a n-queens game state  
'''
def Minimax_Decision(variation, state):
    if variation.is_maxs_turn(state):
        return max_decision(variation, state)
    else:
        return min_decision(variation, state)