# This Python file uses the following encoding: utf-8
import sys

import pygame
import random
import Pawn
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSlider,QLabel
from PySide6.QtCore import QTimer

class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt

class Game:
    white = (255,255,255)
    black = (0, 0 ,0)
    board = (171 , 79,9)
    grid = []
    width:int
    height:int
    margin = 5
    def __init__(self):
        pygame.init()
        self.gameInit()
        self.timer = Timer()
        self.width= 1000 / 8
        self.height = 720 / 8
        self.playerImageSrc = "images/RedPawn.png"
        self.aiImageSrc = "images/GreyPawn.png"
        self.should_quit = False
        self.up_key_pressed = False
        self.down_key_pressed = False

    def changeDifficulty(self, Gamedifficulty):
        self.difficulty = Gamedifficulty

    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime()

        self.process_input()
        self.gameLogic(dt)
        self.render()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.up_key_pressed = True
                if event.key == pygame.K_s:
                    self.down_key_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.up_key_pressed = False
                if event.key == pygame.K_s:
                    self.down_key_pressed = False

    def gameInit(self):
        self.size = self.width, self.height = 625, 450
        self.src = pygame.display.set_mode([50,50])
        self.boards = {"0101010101000002020202020"}
        #for pawns in range(12):
            #self.PlayerPawns.append(Pawn())
        for row in range(5):
            self.grid.append([])
            for column in range(5):
                self.grid[row].append(0)
        self.started = False

        self.screen = pygame.display.set_mode(self.size)

    def gameLogic(self, dt):
        #player behaviour
        #ai behaviour
        pass

    def render(self):
        self.screen.fill(self.board)
        for row in range(5):
            for column in range(5):
                if(row % 2 == 0):
                    if(column % 2 == 1):
                        self.color = self.white
                    else:
                        self.color = self.black
                if(row % 2 == 1):
                    if(column % 2 == 0):
                        self.color = self.white
                    else:
                        self.color = self.black
                pygame.draw.rect(self.src, self.color, [self.width * column, self.height * row , self.width, self.height])
        counter = 0
        for c in "0101010101000002020202020":
            if c == "0":
                #drawing nothing
                pass
            if c == "1":
                imp = pygame.image.load(self.aiImageSrc).convert()
                imp = pygame.transform.scale(imp,(75,75))
                if counter % 2 == 0:
                    self.src.blit(imp, ((counter % 5) * 75 + (2 * counter), 30))
                    print(counter)
                if counter % 2 == 1:
                    self.src.blit(imp, ((counter % 5) * 75 + (3 * counter), 10))
            if c == "2":
                imp = pygame.image.load(self.playerImageSrc).convert()
                imp = pygame.transform.scale(imp,(75,75))
                if counter % 2 == 0:
                    self.src.blit(imp, ((counter % 5) * 75 + (2 * counter), 225))
                if counter % 2 == 1:
                    self.src.blit(imp, ((counter % 5) * 75 + (2 * counter), 300))
            counter += 1
        pygame.display.flip()

class Window(QWidget):
    started:bool
    def __init__(self, game):
        super().__init__()
        self.started = False
        self.game = game
        self.initUi()
        self.init_pygame(self.game)


    def init_pygame(self, game):
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

    def pygame_loop(self):
        if self.game.loop():
            self.close()

    def initUi(self):
        self.setWindowTitle("Py pong")
        self.setGeometry(0,400,300,200)


        self.button = QPushButton("Start Game", self)
        self.button.move(100, 150)
        self.button.clicked.connect(self.OnClick)

        #settings for ai
        self.label1 = QLabel("AI difficulty", self)
        self.label1.move(80, 85)

        self.aislider = QSlider(self)
        self.aislider.sliderReleased.connect(self.OnSlider)
        self.aislider.setRange(1, 3)
        self.aislider.setSingleStep(1)
        self.aislider.move(100, 1)

        self.show()

    def OnClick(self):
        self.started = True
        pass

    def returnStart(self):
        return self.started

    def returnDifficulty(self):
        return self.slider.TickPosition

    def OnSlider(self):
        slider:QSlider = self.sender()
        #self.game.changeDifficulty(slider.value())
        print(slider.value())
        pass

def main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)

    app.setActiveWindow(exe)
    # ...
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
