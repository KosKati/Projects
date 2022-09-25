import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Bad Soden Video Scout"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("Soden.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def ClickMe(self):
        print("Hello World")
        sys.exit()

    def createLayout(self):
        self.groupBox = QGroupBox("What ist your Favorite Sport ?")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Football", self)
        button.clicked.connect(self.ClickMe)
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Volleyball", self)
        button1.clicked.connect(self.ClickMe)
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
