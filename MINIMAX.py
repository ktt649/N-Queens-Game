#Kody Tomochko
#ktt649 # 11156316
#CMPT 317
#Assignment 4
#MINIMAX Files

''' BASIC MINIMAX ALGORITHM FUNCTIONS'''

'''
Returns: best value for player 1 (max)
variation: the n-queens game variation that you want to use
state: a n-queens game state
'''
def Max_Value_basic(variation, state):
    if variation.is_terminal(state):
        best = variation.utility(state)
    else:
        # If at cutoff limit, estimate utility
        if variation.cutoff_test(state, variation.getLimit()):
            best = variation.eval(state)
        else:
            best = variation._negInf
            actions = variation.actions(state)
            for act in actions:
                res = variation.result(state, act)
                val = Min_Value_basic(variation,res)
                if val > best:
                    best = val
    return best


'''
Returns: best value for player 2 (min)
variation: the n-queens game variation that you want to use
state: a n-queens game state
'''
def Min_Value_basic(variation, state):
    if variation.is_terminal(state):
        best = variation.utility(state)
    else:
        # If at cutoff limit, estimate utility
        if variation.cutoff_test(state, variation.getLimit()):
           best =  variation.eval(state)
        else:
            best = variation._posInf
            actions = variation.actions(state)
            for act in actions:
                res = variation.result(state, act)
                val = Max_Value_basic(variation,res)
                if val < best:
                    best = val
    return best


'''
Implements the "no bells and whistles" MiniMax algorithm
Returns: a tuple (minimax, bestMove)
variation: the n-queens game variation that you want to use
state: a n-queens game state
'''
def Minimax_Decision_basic(variation, state):
    best_action = None
    if variation.is_maxs_turn(state):
        best = variation._negInf
        actions = variation.actions(state)
        for act in actions:
            res = variation.result(state, act)
            val = Min_Value_basic(variation, res)
            if val > best:
                best = val
                best_action = act
    else:
        best = variation._posInf
        actions = variation.actions(state)
        for act in actions:
            res = variation.result(state, act)
            val = Max_Value_basic(variation, res)
            if val < best:
                best = val
                best_action = act

    return best, best_action