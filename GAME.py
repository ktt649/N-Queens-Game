#Version Game File

import time
import math
import random
import MINIMAX as minimax
import AB_PRUNING as AB_Prune



def printChart():
    print()
    print("Size   Minimax Value   Best Opening Move   Time in Seconds")
    print("___________________________________________________________")


#GENERAL GAME CLASS
class Game:

    '''
        Game board will be represented as a 1D array
        Each column will be represented as a position in the array
        The queen position for that column will be represented by the value in that position
        example: [1, 3, 0, 2] would represent a game board as such: (can be seen by calling printBoard(board_list)
                    -, -, Q, -
                    Q, -, -, -
                    -, -, -, Q
                    -, Q, -, -

    '''
    #For no limit search, limit = inf
    def __init__(self, size, prune, limit = math.inf, interactive = False, board = []):
        self._negInf = -math.inf
        self._posInf = math.inf
        self._gameSize = size
        self._board = board
        self._limit = limit
        self._prune = prune

        if not interactive:
            self.runGame(prune)

    def updateBoard(self, board):
        self._board = board

    def playMove(self, cutoff):
        self._limit = cutoff
        if self._prune:
            result = AB_Prune.Minimax_Decision(self, self._board)
            self._board.append(result[1])
        else:
            result = minimax.Minimax_Decision_basic(self, self._board)
            self._board.append(result[1])
        return result[1]


    def runGame(self, prune):
        #RUN
        start_time = time.time()
        if prune:
            result = AB_Prune.Minimax_Decision(self, self._board)
        else:
            result = minimax.Minimax_Decision_basic(self, self._board)
        finish_time = time.time()

        # DATA
        runTime = finish_time - start_time
        bestOpeningMove = ("X",result[1])
        minimaxValue = result[0]

        self.printDataTable(self._gameSize, minimaxValue, bestOpeningMove, runTime)


    '''
        prints data for this iteration of the game
    '''
    def printDataTable(self, size, value, openMove, time):
        if not value == int(value):
            if size >= 10 :
                print("", size, "    ", "{0:.4f}".format(value), "       ", openMove, "       ", "{0:.8f}".format(time))
            elif value < 0:
                print(" ", size, "    ", "{0:.4f}".format(value), "       ", openMove, "       ", "{0:.8f}".format(time))
            else:
                print(" ", size, "     ", "{0:.4f}".format(value), "       ", openMove, "       ", "{0:.8f}".format(time))

        elif value > 0:
            if size >= 10:
                print("",size,"       ", value, "          ", openMove, "       ", "{0:.8f}".format(time))
            else:
                print(" ", size, "       ", value, "          ", openMove, "       ", "{0:.8f}".format(time))
        else:
            if size >= 10:
                print("", size, "      ", value, "          ", openMove, "       ", "{0:.8f}".format(time))
            else:
                print(" ", size, "      ", value, "          ", openMove, "       ", "{0:.8f}".format(time))


    '''
        takes in a board in list form, prints it in a readable form
    '''
    def printBoard(self, board_list):
        size = self._gameSize
        print("-------------------------")
        print()
        # Creating a blank board, "-" represents an empty position
        list_matrix = [["-" for m in range(size)] for n in range(size)]

        # Iterating through row to find the index and the value
        for element in range(size):
            if(element < len(board_list)):
                x = element
                y = board_list[element]

                list_matrix[x][y] = "Q"

        # Looping through length of the board_list
        for row in range(size):
            myArray = [[v.strip() for v in x] for x in list_matrix]
            myArray = [v[row] for v in myArray]

            print(", ".join(myArray))
        print()
        print("-------------------------")


    def check_move(self, board):
        size = len(board)

        #Check rows
        if not len(board) == len(set(board)):
            return False

        #Check columns
        for x in range(size):
            for col in range(x + 1, size):
                if abs(x - col) == abs(board[x] - board[col]):
                    return False
        return True

    '''
        Returns: list of legal actions from a given state
    '''
    def actions(self, state):
        actions = []
        #Create a copy of the state, with length + 1 for new move
        tempBoard = list(state)
        tempBoard.append(0)
        #Check every move
        for i in range(self._gameSize):
            tempBoard[len(state)] = i
            #if it is a legal move, add it to actions
            if self.check_move(tempBoard):
                actions.append(i)
        return actions

    '''
        Returns: a new game state,
        which is the result of taking a given action in the given state
    '''
    def result(self, state, action):
        newState = list(state)
        newState.append(action)
      #  print("state: " + str(newState))
      #  self.printBoard(newState)
        return newState

    '''
        Returns: boolean
        True if the given state has no more legal moves
    '''
    def is_terminal(self, state):
        numberOfMoves = len(state)
        if numberOfMoves >= self._gameSize or not self.actions(state):
            return True
        else:
            return False

    '''
        Returns: boolean
        True if Player 1's turn (Max)
        False if Player 2's turn (Min)
    '''
    def is_maxs_turn(self, state):
        if len(state) % 2 == 0:
            return True
        else:
            return False


    def getLimit(self):
        return self._limit

    def cutoff_test(self, state, depth):
        if len(state) >= depth:
            return True

#GAME CLASS FOR VARIATION A
class VariationA(Game):
    '''
        Returns: a numeric value representing the "final score"
        The state must be a terminal state
    '''
    def utility(self, state):
        if self.is_terminal(state):
            #If it should be player 1's turn next
            if self.is_maxs_turn(state):
                # player 2 wins!
                return -1
            else:
                # player 1 wins!
                return 1


	#Returns a random estimate of the minimax value.
    def eval(self, state):
        return round(random.uniform(-1.0, 1.0),4)

#GAME CLASS FOR VARIATION B
class VariationB(Game):
    '''
        Returns: a numeric value representing the "final score"
        The state must be a terminal state
    '''
    def utility(self, state):
        if self.is_terminal(state):
            #If it should be player 1's turn next
            if self.is_maxs_turn(state):
                # player 2 wins! (min)
                return -len(state)
            else:
                # player 1 wins! (max)
                return len(state)
	
	#Returns a random estimate of the minimax value.
    def eval(self, state):
        return round(random.uniform(-self._gameSize, self._gameSize),4)