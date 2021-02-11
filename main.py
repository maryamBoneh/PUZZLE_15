import sys
import os

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from functools import partial
from numpy import random

global XY
XY = [[0, 0], [0, 60], [0, 120], [0, 180], [60, 0], [60, 60], [60, 120], [60, 180], [
      120, 0], [120, 60], [120, 120], [120, 180], [180, 0], [180, 60], [180, 120], [180, 180]]


class puzzle15(QWidget):
    def __init__(self):
        super(puzzle15, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()

        self.chinesh()

        self.ui.btn_one.clicked.connect(
            partial(self.click_btn, '1', self.ui.btn_one.x(), self.ui.btn_one.y()))
        self.ui.btn_two.clicked.connect(
            partial(self.click_btn, '2', self.ui.btn_two.x(), self.ui.btn_two.y()))
        self.ui.btn_three.clicked.connect(
            partial(self.click_btn, '3', self.ui.btn_three.x(), self.ui.btn_three.y()))
        self.ui.btn_four.clicked.connect(
            partial(self.click_btn, '4', self.ui.btn_four.x(), self.ui.btn_four.y()))
        self.ui.btn_five.clicked.connect(
            partial(self.click_btn, '5', self.ui.btn_five.x(), self.ui.btn_five.y()))
        self.ui.btn_six.clicked.connect(
            partial(self.click_btn, '6', self.ui.btn_six.x(), self.ui.btn_six.y()))
        self.ui.btn_seven.clicked.connect(
            partial(self.click_btn, '7', self.ui.btn_seven.x(), self.ui.btn_seven.y()))
        self.ui.btn_eight.clicked.connect(
            partial(self.click_btn, '8', self.ui.btn_eight.x(), self.ui.btn_eight.y()))
        self.ui.btn_nine.clicked.connect(
            partial(self.click_btn, '9', self.ui.btn_nine.x(), self.ui.btn_nine.y()))
        self.ui.btn_ten.clicked.connect(
            partial(self.click_btn, '10', self.ui.btn_ten.x(), self.ui.btn_ten.y()))
        self.ui.btn_eleven.clicked.connect(
            partial(self.click_btn, '11', self.ui.btn_eleven.x(), self.ui.btn_eleven.y()))
        self.ui.btn_twelve.clicked.connect(
            partial(self.click_btn, '12', self.ui.btn_twelve.x(), self.ui.btn_twelve.y()))
        self.ui.btn_thirteen.clicked.connect(
            partial(self.click_btn, '13', self.ui.btn_thirteen.x(), self.ui.btn_thirteen.y()))
        self.ui.btn_fourteen.clicked.connect(
            partial(self.click_btn, '14', self.ui.btn_fourteen.x(), self.ui.btn_fourteen.y()))
        self.ui.btn_fifteen.clicked.connect(
            partial(self.click_btn, '15', self.ui.btn_fifteen.x(), self.ui.btn_fifteen.y()))


    def chinesh(self):
        global XY
        global empty
        random.shuffle(XY)

        self.ui.btn_one.move(int(XY[0][0]), int(XY[0][1]))
        self.ui.btn_two.move(int(XY[1][0]), int(XY[1][1]))
        self.ui.btn_three.move(int(XY[2][0]), int(XY[2][1]))
        self.ui.btn_four.move(int(XY[3][0]), int(XY[3][1]))
        self.ui.btn_five.move(int(XY[4][0]), int(XY[4][1]))
        self.ui.btn_six.move(int(XY[5][0]), int(XY[5][1]))
        self.ui.btn_seven.move(int(XY[6][0]), int(XY[6][1]))
        self.ui.btn_eight.move(int(XY[7][0]), int(XY[7][1]))
        self.ui.btn_nine.move(int(XY[8][0]), int(XY[8][1]))
        self.ui.btn_ten.move(int(XY[9][0]), int(XY[9][1]))
        self.ui.btn_eleven.move(int(XY[10][0]), int(XY[10][1]))
        self.ui.btn_twelve.move(int(XY[11][0]), int(XY[11][1]))
        self.ui.btn_thirteen.move(int(XY[12][0]), int(XY[12][1]))
        self.ui.btn_fourteen.move(int(XY[13][0]), int(XY[13][1]))
        self.ui.btn_fifteen.move(int(XY[14][0]), int(XY[14][1]))
        empty = [XY[15][0], XY[15][1]]


    def click_btn(self, btn, x, y):
        global empty
        print('self, btn, x, y ', btn, x, y)
        if (empty[0] == x):
            if (empty[1] - y == 60 or empty[1] + 60 == y):
                print('x: ', x, 'y: ', y, 'empty: ', empty, 'btn: ', btn)
                self.move_btn(btn, x, y)
        elif (empty[1] == y):
            if (empty[0] - x == 60 or empty[0] + 60 == x):
                print('x: ', x, 'y: ', y, 'empty: ', empty, 'btn: ', btn)
                self.move_btn(btn, x, y)

    def move_btn(self, btn, x, y):
        global empty

        if btn == '1':
            self.ui.btn_one.move(int(empty[0]), int(empty[1]))
        elif btn == '2':
            self.ui.btn_two.move(int(empty[0]), int(empty[1]))
        elif btn == '3':
            self.ui.btn_three.move(int(empty[0]), int(empty[1]))
        elif btn == '4':
            self.ui.btn_four.move(int(empty[0]), int(empty[1]))
        elif btn == '5':
            self.ui.btn_five.move(int(empty[0]), int(empty[1]))
        elif btn == '6':
            self.ui.btn_six.move(int(empty[0]), int(empty[1]))
        elif btn == '7':
            self.ui.btn_seven.move(int(empty[0]), int(empty[1]))
        elif btn == '8':
            self.ui.btn_eight.move(int(empty[0]), int(empty[1]))
        elif btn == '9':
            self.ui.btn_nine.move(int(empty[0]), int(empty[1]))
        elif btn == '10':
            self.ui.btn_ten.move(int(empty[0]), int(empty[1]))
        elif btn == '11':
            self.ui.btn_eleven.move(int(empty[0]), int(empty[1]))
        elif btn == '12':
            self.ui.btn_twelve.move(int(empty[0]), int(empty[1]))
        elif btn == '13':
            self.ui.btn_thirteen.move(int(empty[0]), int(empty[1]))
        elif btn == '14':
            self.ui.btn_fourteen.move(int(empty[0]), int(empty[1]))
        else:
            self.ui.btn_fifteen.move(int(empty[0]), int(empty[1]))

        empty = [x, y]
        print(' empty = [x, y]: ', empty)


if __name__ == "__main__":
    app = QApplication([])
    widget = puzzle15()
    widget.show()
    sys.exit(app.exec_())
