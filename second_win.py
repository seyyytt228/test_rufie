from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
app = QApplication([])
win = QWidget()
class TestWin(QWidget):
    def __init__(self):
        super(). __init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.next_click()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.btn1 = QLabel('Введите Ф.И.О.:')
        self.btn2 = QLabel('Полных лет:')
        self.btn3 = QLabel(txt_test1)
        self.btn4 = QLabel(txt_test2)
        self.btn5 = QLabel(txt_test3)
        self.bt6timer = QLabel('00:00:15')

        self.pb1 = QPushButton(txt_starttest1)
        self.pb2 = QPushButton(txt_starttest2)
        self.pb3 = QPushButton(txt_starttest3)
        self.pb4 = QPushButton(txt_sendresults)

        self.line1 = QLineEdit(txt_hintname)
        self.line2 = QLineEdit(txt_hintage)
        self.line3 = QLineEdit(txt_hinttest1)
        self.line4 = QLineEdit(txt_hinttest2)
        self.line5 = QLineEdit(txt_hinttest3)


        self.l_line.addWidget(self.btn1)
        self.l_line.addWidget(self.line1)
        self.l_line.addWidget(self.btn2)
        self.l_line.addWidget(self.line2)
        self.l_line.addWidget(self.btn3)
        self.l_line.addWidget(self.pb1)
        self.l_line.addWidget(self.line3)
        self.l_line.addWidget(self.btn4)
        self.l_line.addWidget(self.line4)
        self.l_line.addWidget(self.pb2)
        self.l_line.addWidget(self.btn5)
        self.l_line.addWidget(self.pb3)
        self.l_line.addWidget(self.line5)

        self.r_line.addWidget(self.bt6timer)

        self.h_line.addWidget(self.pb4, alignment = Qt.AlignCenter)

        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)


    def connects(self):
        self.pb4.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        #self.tw = FinalWin()


    #def.show(self):
     #   pass

#index = 4 * (self.line3 + self.line4 + self.line5) - 200   
#index_rufe = index / 10

win.show()
win = TestWin()

app.exec_()
