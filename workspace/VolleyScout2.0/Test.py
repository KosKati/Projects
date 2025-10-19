
import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel,  QFormLayout, QPushButton, QGroupBox, QLineEdit, QDateEdit,QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path
import os.path


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)

        
        script_dir  = Path(__file__)
        script_dir  = Path(__file__).parent
        print(script_dir)
        path  = Path(script_dir, "Images")
        print(path)
        directory = '.\\Teams\\'
        filename = "Volleyball_Half_Court.png"
        file_path = os.path.join(path, filename)
        
        label = QLabel(self)
        pixmap = QPixmap( "Pics/Volleyball_Half_Court.png")
        label.setPixmap(pixmap)
        parentlayout = QGridLayout()
        label0 = QLabel("")
        label1 = QLabel("Pos 1")
        parentlayout.addWidget(label0, 0, 0)
        parentlayout.addWidget(label1, 0,1)
        label2 = QLabel("Pos 2")
        label.setLayout(parentlayout)


        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())
    

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
    
    

