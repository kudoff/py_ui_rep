import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.run)
        self.ellipse = False

    def run(self):
        self.ellipse = True
        self.update()

    def paintEvent(self, event):
        QMainWindow.paintEvent(self, event)
        if self.ellipse:
            painter = QPainter(self)
            brush = QBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
            painter.setBrush(brush)
            size = self.size()
            x, y = randint(1, size.height()), randint(1, size.width())
            r = randint(1, 100)
            painter.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
