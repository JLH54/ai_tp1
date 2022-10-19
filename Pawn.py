# This Python file uses the following encoding: utf-8


class Pawn:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.imgsrc = img
        self.alive = True
        self.isKing = False
        pass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def SetKing(self):
        self.isKing = True
