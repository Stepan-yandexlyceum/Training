from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import random
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.draw())
        self.qp = QPainter()

    def paint(self):
        self.qp.repaint()

    def paintEvent(self, event):
        self.draw()
        self.qp.begin(self)
        self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(245, 237, 20))
        randnum = random.randint(0, 100)
        self.qp.drawEllipse(self.coords[0] - randnum, self.coords[1] - randnum, self.coords[0] + randnum,
                            self.coords[1] + randnum)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
