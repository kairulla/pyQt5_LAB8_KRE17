#!/usr/bin/env python3
# coding=utf-8

from random import randint
import sys
import re

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.uic import loadUi


class Launcher(QWidget):

    def __init__(self):
        super(Launcher, self).__init__()
        loadUi('g.ui', self)

        self.setWindowTitle('Лабораторная 8 _ Python3 + PyQt5')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('_MY_PICTURES//logo.png'))
        self.qLabelPicturePrimer.setPixmap(QPixmap('_MY_PICTURES//PRIMER_YELLOW.png'))

        image = QtGui.QPixmap()
        image.load('_MY_PICTURES//background.png')
        # image = image.scaled(self.width(), self.height())
        image = image.scaledToWidth(round(self.width() / 14))
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        self.qPushButtonClear.clicked.connect(self.qPushButtonClearOnClick)
        self.qPushButtonExit.clicked.connect(self.close)
        self.qPushButtonRandom.clicked.connect(self.qPushButtonRandomOnClick)
        self.qPushButtonSolver.clicked.connect(self.qPushButtonSolverOnClick)


    def qPushButtonClearOnClick(self):
        self.qTableWidget.clearContents()


    def qPushButtonRandomOnClick(self):
        self.qPushButtonClearOnClick()
        j = 0
        while j < self.qTableWidget.columnCount():
            random_num = randint(-100, 100)
            self.qTableWidget.setItem(0, j, QTableWidgetItem(str(random_num)))
            j += 1


    def qPushButtonSolverOnClick(self):
        pass



app = QApplication(sys.argv)
window = Launcher()
window.show()
sys.exit(app.exec_())
