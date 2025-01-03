#! /usr/bin/python3

from tkinter import *
import copy
import time

WIDTH = 1000
HEIGHT = 1000

class ChessPiece:
    def __init__(self, color, side, posx, posy, linear):
        self.color = color
        self.side = side
        self.cut = False
        self.posx = posx
        self.posy = posy
        self.linear = linear
        self.allMoves = None
        self.allAvailableMoves = None
    def getPosition(self):
        return (self.posx, self.posy)
    def isLinear(self):
        return self.linear

class Pawn(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, False)
        self.allMoves = [(0, 1)]
        self.allAvailableMoves = None
    def __repr__(self):
        return "Pawn(ChessPiece)"

class King(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, False)
        self.allMoves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        self.allAvailableMoves = None
    def __repr__(self):
        return "King(ChessPiece)"

class Knight(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, False)
        self.allMoves = [(1, 2), (2, 1), (-2, 1), (1, -2), (-1, 2), (2, -1), (-2, -1), (-1, -2)]
        self.allAvailableMoves = None
    def __repr__(self):
        return "Knight(ChessPiece)"

class Queen(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, True)
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        self.allAvailableMoves = None
    def __repr__(self):
        return "Queen(ChessPiece)"

class Castle(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, True)
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.allAvailableMoves = None
    def __repr__(self):
        return "Castle(ChessPiece)"

class Bishop(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, True)
        self.directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        self.allAvailableMoves = None
    def __repr__(self):
        return "Bishop(ChessPiece)"

class OccupancyGrid:
    def __init__(self):
        self.columns = [[0 for x in range(8)] for y in range(8)]
    def occupySquare(self, x, y):
        self.columns[x][y] = 1
    def unoccupySquare(self, x, y):
        self.columns[x][y] = 0
    def occupyRow(self, y):
        for i in range(8):
            self.columns[i][y-1] = 1
    def unoccupyRow(self, y):
        for i in range(8):
            self.columns[i][y-1] = 0
    def occupyColumn(self, x):
        self.columns[x-1] = [1 for i in range(8)]
    def unoccupyColumn(self, x):
        self.columns[x-1] = [0 for i in range(8)]
    def reset(self):
        self.columns = [[0 for x in range(8)] for y in range(8)]
    def display(self):
        for y in self.columns:
            print(y)
    def isOccupiedAt(self, x, y):
        return self.columns[x-1][y-1] == 1 if (x in range(1, 9) and y in range(1, 9)) else False
    def flip(self):
        for x in range(len(self.columns)):
            self.columns[x] = list(reversed(self.columns[x]))

class ChessGridInterface:
    def __init__(self, player, c):
        self.columns = [[] for y in range(8)]
        black = False
        for y in range(8):
            for x in range(8):
                self.columns[y].append(c.create_rectangle(WIDTH*(x+1)/10, HEIGHT*(8-y)/10, WIDTH*(x+2)/10, HEIGHT*(9-y)/10, fill=("black" if black else "white")))
                black = not black
                tk.update()
                time.sleep(0.1)
            black = not black

class Player:
    def __init__(self, side, color, opponent=None):
        self.side = side
        self.color = color
        self.pawns = [Pawn(self.color, self.side, i+1, 2) for i in range(8)]
        self.castles = [Castle(self.color, self.side, 1, 1), Castle(self.color, self.side, 8, 1)]
        self.knights = [Knight(self.color, self.side, 2, 1), Knight(self.color, self.side, 7, 1)]
        self.bishops = [Bishop(self.color, self.side, 3, 1), Bishop(self.color, self.side, 6, 1)]
        self.king = King(self.color, self.side, 4, 1) if side == "up" else King(self.color, self.side, 5, 1)
        self.queen = Queen(self.color, self.side, 5, 1) if side == "up" else Queen(self.color, self.side, 4, 1)
        self.pieces = [self.king, self.queen] + self.castles + self.knights + self.pawns + self.bishops
        self.occupancyGridSelf = OccupancyGrid()
        self.occupancyGridSelf.occupyRow(1)
        self.occupancyGridSelf.occupyRow(2)
        self.opponent = opponent
        self.occupancyGridOpp = OccupancyGrid()
        if opponent != None:
            self.occupancyGridOpp = copy.deepcopy(self.opponent.occupancyGridSelf)
            self.occupancyGridOpp.flip()
    def updateOppOccupancy(self, opponent=None):
        if opponent != None:
            self.opponent = opponent
        self.occupancyGridOpp = copy.deepcopy(self.opponent.occupancyGridSelf)
        self.occupancyGridOpp.flip()
    def updateSelfOccupancy(self):
        self.occupancyGridSelf.reset()
        for piece in self.pieces:
            coords = piece.getPosition()
            self.occupancyGridSelf.occupySquare(coords[0]-1, coords[1]-1)
    def setAvailableMoves(self):
        # Set allAvailableMoves for queen, bishops and castles given directions and spaces available
        # Set allAvailableMoves for king, knights and pawns given allMoves and spaces available
        # Subtract opposing player's occupied spaces, spaces occupied by own pieces and spaces outside grid from allMoves and spaces
        # in all directions
        piece = self.pieces[5]
        for piece in self.pieces:
            if piece.isLinear():
                piece.allAvailableMoves = []
                for direction in piece.directions:
                    cnt = 1
                    move = direction
                    posAfterMove = tuple([piece.getPosition()[i]+move[i] for i in range(len(move))])
                    while posAfterMove[0] in range(1, 9) and posAfterMove[1] in range(1, 9)\
                          and not self.occupancyGridOpp.isOccupiedAt(posAfterMove[0], posAfterMove[1])\
                          and not self.occupancyGridSelf.isOccupiedAt(posAfterMove[0], posAfterMove[1]):
                        piece.allAvailableMoves.append(move)
                        cnt += 1
                        move = tuple([direction[i]*cnt for i in range(len(direction))])
                        posAfterMove = tuple([piece.getPosition()[i]+move[i] for i in range(len(move))])
            else:
                piece.allAvailableMoves = []
                for move in piece.allMoves:
                    posAfterMove = tuple([piece.getPosition()[i]+move[i] for i in range(len(move))])
                    if posAfterMove[0] in range(1, 9) and posAfterMove[1] in range(1, 9)\
                       and not self.occupancyGridOpp.isOccupiedAt(posAfterMove[0], posAfterMove[1])\
                       and not self.occupancyGridSelf.isOccupiedAt(posAfterMove[0], posAfterMove[1]):
                        piece.allAvailableMoves.append(move)

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

computer = Player("up", "black")
user = Player("down", "white", computer)
computer.updateOppOccupancy(user)

user.pawns[5].posy += 2
user.updateSelfOccupancy()
computer.updateOppOccupancy()

computer.knights[1].posx -= 1
computer.knights[1].posy += 2
computer.updateSelfOccupancy()
user.updateOppOccupancy()

#for x in range(9):
#    canvas.create_line(WIDTH*(x+1)/10, HEIGHT/10, WIDTH*(x+1)/10, HEIGHT*9/10, width=3)
#
#for x in range(9):
#    canvas.create_line(WIDTH/10, HEIGHT*(x+1)/10, WIDTH*9/10, HEIGHT*(x+1)/10, width=3)

a = ChessGridInterface(user, canvas)

canvas.mainloop()
