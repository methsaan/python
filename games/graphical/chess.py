#! /usr/bin/python3

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

class Pawn(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, False)
        self.allMoves = [(0, 1)]
        self.allAvailableMoves = None

class King(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, False)
        self.allMoves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        self.allAvailableMoves = None

class Knight(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, False)
        self.allMoves = [(1, 2), (2, 1), (-2, 1), (1, -2), (-1, 2), (2, -1), (-2, -1), (-1, -2)]
        self.allAvailableMoves = None

class Queen(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, True)
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        self.allAvailableMoves = None

class Castle(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, True)
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.allAvailableMoves = None

class Bishop(ChessPiece):
    def __init__(self, color, side, posx, posy):
        super().__init__(color, side, posx, posy, True)
        self.directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        self.allAvailableMoves = None

class OccupancyGrid:
    def __init__(self):
        self.columns = [[0 for x in range(8)] for y in range(8)]
    def occupySquare(self, x, y):
        self.columns[x][y] = 1
    def unoccupySquare(self, x, y):
        self.columns[x][y] = 0
    def occupyRow(self, y):
        for i in range(8):
            self.columns[i][y] = 1
    def unoccupyRow(self, y):
        for i in range(8):
            self.columns[i][y] = 0
    def occupyColumn(self, x):
        self.columns[x] = [1 for i in range(8)]
    def unoccupyColumn(self, x):
        self.columns[x] = [0 for i in range(8)]
    def reset(self):
        self.columns = [[0 for x in range(8)] for y in range(8)]

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
            self.occupancyGridOpp = self.opponent.occupancyGridSelf
    def updateOppOccupancy(self, opponent=None):
        if opponent != None:
            self.opponent = opponent
        self.occupancyGridOpp = self.opponent.occupancyGridSelf
    def updateSelfOccupancy(self):
        self.occupancyGridSelf.reset()
        for piece in self.pieces:
            coords = piece.getPosition()
            self.occupancyGridSelf.occupySquare(coords[0], coords[1])
    #def setAvailableMoves(self):
        # Set allAvailableMoves for queen, bishops and castles given directions and spaces available
        # Set allAvailableMoves for king, knights and pawns given allMoves and spaces available
        # Subtract opposing player's occupied spaces, spaces occupied by own pieces and spaces outside grid from allMoves and spaces
        # in all directions


from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

computer = Player("up", "black")
user = Player("down", "white", computer)
computer.updateOppOccupancy(user)

user.pawns[5].posy += 2
user.updateSelfOccupancy()
computer.updateOppOccupancy()

computer.knight[1].posx -= 1
computer.knight[1].posy += 2
computer.updateSelfOccupancy()
user.updateOppOccupancy()

for i in user.occupancyGridSelf:
    print(i)

for i in computer.occupancyGridSelf:
    print(i)

canvas.mainloop()
