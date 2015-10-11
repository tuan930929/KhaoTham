#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class changeVisibility(QWidget):    
    def __init__(self, parent=None):        
        super(changeVisibility, self).__init__(parent)

        self.textbrowserA = QTextBrowser()
        self.textbrowserA.setStyleSheet("background-color:red")

        self.textbrowserB = QTextBrowser()
        self.textbrowserB.setStyleSheet("background-color:blue")


        self.buttonA = QPushButton("Show A")
        self.buttonB = QPushButton("Show B")

        self.verticalLayout = QVBoxLayout(self)

        self.buttonA = QPushButton("Show A")

        self.verticalLayout.addWidget(self.textbrowserA)
        self.textbrowserA.show()
        self.verticalLayout.addWidget(self.textbrowserB)
        self.textbrowserB.hide()

        self.verticalLayout.addWidget(self.buttonA)
        self.verticalLayout.addWidget(self.buttonB)

        self.buttonA.clicked.connect(self.showA)
        self.buttonB.clicked.connect(self.showB)

    def showA(self):
        self.textbrowserB.hide()
        self.textbrowserA.show()

    def showB(self):
        self.textbrowserA.hide()
        self.textbrowserB.show()


def main():
    app = QApplication(sys.argv)
    cV = changeVisibility()
    cV.show()
    app.exec_()


if __name__ == '__main__':
    main()