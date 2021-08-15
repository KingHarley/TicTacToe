import numpy
import os
#import agent.agent

print(os.getcwd())

# board = numpy.zeros((3,3), dtype=numpy.int)

# def clearBoard():
#     board.fill(0)
#     print(board)
#     return 0

# def checkWin(player):
#     for i in range(3):
#         if(board[:,i].all() == player or board[i,:].all() == player):
#             clearBoard()
#             return 1
#     if(board[1,1] == player and ((board[0,0] == player and board[2,2] == player) or (board[0,2] == player and board[2,0] == player))):
#             clearBoard()
#             return 1
#     return 0
                                

# def makeMove(row, column, player):
#     if(board[row, column] == 0):
#         board[row, column] = player
#         return checkWin(player)
#     else:
#         return -1

class tictactoe():

    def __init__(self, player, opponent="random"):
        self.state = numpy.zeros(9, dtype=int)
        self.finished = False
        self.player = player
        self.opponent = agent(opponent)

    def step(self, action):
        if(self.state[action] != 0):
            self.finished = True
            return -10
        else:
            self.state[action] = self.player
            self.opponent.agent.step(numpy.zeros(3))
            return 1
    
    def render(self):
        pass

    def reset(self):
        pass
