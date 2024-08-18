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
        self.columns = [[0 for x in range(10)] for y in range(10)]

class Player:
    def __init__(self, side, color):
        self.side = side
        self.color = color
        self.pawns = [Pawn(self.color, self.side, i+1, 2) for i in range(8)]
        self.castles = [Castle(self.color, self.side, 1, 1), Castle(self.color, self.side, 8, 1)]
        self.knights = [Knight(self.color, self.side, 2, 1), Knight(self.color, self.side, 7, 1)]
        self.bishops = [Bishop(self.color, self.side, 3, 1), Bishop(self.color, self.side, 6, 1)]
        self.king = King(self.color, self.side, 4, 1) if side == "up" else King(self.color, self.side, 5, 1) 
        self.queen = Queen(self.color, self.side, 5, 1) if side == "up" else Queen(self.color, self.side, 4, 1) 
    def setAvailableMoves(self):
        # Set allAvailableMoves for queen, bishops and castles given directions and spaces available
        # Set allAvailableMoves for king, knights and pawns given allMoves and spaces available

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.mainloop()
