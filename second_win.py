


from PyQt5.QtCore import Qt
from PyQt5.Qtwidgets import QApplication, Qwidget, QHBoxLayout, QVBoxLayout, \
        QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from instr import *
from final_win import *

class Testwin(QWidget):
    def _init_ (self):
        super()._init_()
self.initUI()
self.connects()
self.set_appear()
self.show()
def next_click(self):
    self.tw = Testwin()
    self.hide()
def connects(self):
    self.btn_next.clicked.connect(self.next_click)
def set_appear(self):
    self.setwindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
def initUI(self):

self.btn_next = QPushButton(txt_sendresults, self)
self.btn_test1 = QPushButton(txt starttest1, self)
self.btn_test2 = QPushButton(txt _starttest2, self)
self.btn_test3 = QPushButton(txt starttest3, self)
self.text name QLabel (txt_name)
self.text_age = QLabel(txt_age)
self.text_test1 = QLabel(txt_test1)
self.text_test2 = QLabel(txt_ test2)
self.text_test3 = QLabel(txt test3)
self.text_timer = QLabel(txt timer)
self.line_name = QLineEdit(txt hintname)
self.line_age QLineEdit(txt hintage)
self.line_test1 = QLineEdit(txt_ hinttest1)
self.line_test2 = QLineEdit(txt hinttest2)
self.line_test3 = QLineEdit (txt hinttest3)
self.1 line = QVBoxLayout()
self.r_line = QVBoxLayout()
self.h_line = QHBoxLayout()
self.r_line.addwidget(self.text timer, alignment = Qt.AlignCenter)
self.1_line.addwidget(self.text_name, alignment = Qt.Alignleft)
self.1_line.addwidget(self.line name, alignment = Qt.Alignleft)
self.1_line.addwidget (self.text age, alignment = Qt.Alignleft)
self.1_line.addwidget(self.line age, alignment = Qt.Alignleft)
self.1_line.addwidget(self.text testl, alignment = Qt.Alignleft)
self.1_line.addwidget (self.btn test1, alignment = Qt.Alignleft)
self.1_line.addwidget (self.line test1, alignment = Qt.Alignleft)
self.1_line.addwidget (self.text test2, alignment = 0t.Alignleft)
self.1_line.addwidget (self.btn test2, alignment = Qt.Alignleft)
self.1_line.addwidget(self.text test3, alignment = Qt.Alignleft)
self.1_line.addwidget (self.btn test3, alignment = Qt.Alignleft)
self.1_line.addwidget(self.line test2, alignment = Qt.Alignleft)
self.1_line.addwidget(self.line test3, alignment = Qt.Alignleft)
self.1_line.addwidget(self.btn next, alignment = Qt.Aligncenter)
self.h_line.addlayout (self.1 line)
self.h_line.addlayout (self.r line)
self.setlayout(self.h line)
def next_click(self):
self.hide().
self.fw = Finalwin()
def connects(self):
self.btn next.clicked.connect(self.next_click)
def set_appear(self):
    self.setwindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)