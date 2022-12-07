#!/usr/bin/env python3
# coding=utf-8

from random import randint
import sys
import re

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.uic import loadUi

from TaskSolver import TaskSolver


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
            random_num = randint(-10, 10)
            self.qTableWidget.setItem(0, j, QTableWidgetItem(str(random_num)))
            j += 1

    def qPushButtonSolverOnClick(self):
        resList = []
        try:
            j = 0
            while j < self.qTableWidget.columnCount():
                a = self.qTableWidget.item(0, j).text()
                resList.append(float(a))
                j += 1
            fg = TaskSolver(resList)
            reshenie = fg.getReshenie()
            j = 0
            while j < self.qTableWidget.columnCount():
                y = reshenie[j]
                self.qTableWidget.setItem(1, j, QTableWidgetItem(str("%.4f" % y)))
                # print(y)
                j += 1
        except:
            i = 0
            while i < self.qTableWidget.rowCount():
                j = 0
                while j < self.qTableWidget.columnCount():
                    self.qTableWidget.setItem(i, j, QTableWidgetItem("?"))
                    j += 1
                i += 1


app = QApplication(sys.argv)
window = Launcher()
window.show()
sys.exit(app.exec_())
