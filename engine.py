# This Python file uses the following encoding: utf-8
import sys
import pygame
from PySide6.QtWidgets import QApplication

class Game:
    def __init__(self):
        pygame.init()
        self.gameInit()

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
        self.size = self.width, self.height = 640, 480
        self.black = 0,0,0

        self.screen = pygame.display.set_mode(self.size)

    def gameLogic(self, dt):
        pass

    def render(self):
        self.screen.fill(self.black)

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

        self.slider = QSlider(self)
        self.slider.sliderReleased.connect(self.OnSlider)
        self.slider.setRange(1, 3)
        self.slider.setSingleStep(1)


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
        self.game.changeDifficulty(slider.value())
        print(slider.value())
        pass

class engine:
    id = [[]]
    def __init__(self):
        game = Game()
        exe = Window(game)
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



