# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication

import engine

def main():
    app = QApplication(sys.argv)

    Engine = engine()

    Engine.initScreen()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()