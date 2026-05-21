from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt_index = QLabel(txt_index, index_rufie)
        self.txt_workheart = QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_index)
        self.layout.addWidget(self.txt_workheart)
        self.setLayout(self.layout)
        self.layout.addWidget(self.txt_index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.txt_workheart, alignment = Qt.AlignCenter)

    def results(self):
        index_rufie = (4*(txt_hinttest1+txt_hinttest2+txt_hinttest3)-200)/10

app = QApplication([])
mw = FinalWin()
app.exec_()
