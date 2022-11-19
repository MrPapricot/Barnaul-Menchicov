import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QBrush, QPainter, QColorConstants
from PyQt5.QtCore import QPoint
from random import randint


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('Ui.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.button_pressed)

    def paintEvent(self, event) -> None:
        if self.do_paint:
            qp = QPainter(self)
            qp.setBrush(QBrush(QColor(QColorConstants.Yellow)))
            self.drawer(qp)
        self.do_paint = False

    def drawer(self, qp: QPainter):
        a = randint(3, 50)
        qp.drawEllipse(QPoint(self.width() // 2, self.height() // 2), a, a)

    def button_pressed(self):
        print('kajg')
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())
