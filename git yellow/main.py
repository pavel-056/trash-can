import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("Circle")

        button = QPushButton('Нажми', self)
        button.clicked.connect(self.draw)
        button.resize(100, 50)
        button.move(250, 250)
        self.line = QLine()

    def paintEvent(self,event):
        QMainWindow.paintEvent(self, event)
        if not self.line.isNull():
            painter = QPainter(self)
            pen = QPen(Qt.yellow, 3)
            painter.setPen(pen)
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            x, y = randint(0, 300), randint(0, 300)
            painter.drawEllipse(x, x, y, y)

    def draw(self):
        button = self.sender()
        self.line = QLine(QPoint(), button.pos())
        self.update()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())