# This Python file uses the following encoding: utf-8
import sys
import pygame

class engine:
    id = [[]]
    def __init__(self):

        pass

    def initEngine(self):
        for i in range(0,8):
            for j in range(0, 8):
                pass
                #self.id[i][j] =
        pass

    def initScreen(self):
        self.size = self.width, self.height = 640, 480
        self.board = 139, 69,19
        self.whiteTile = 255, 255 ,224
        self.greenTile = 50, 50 ,0
        self.setWindowTitle("Checkers")
        self.setGeometry(0,400,300,200)

