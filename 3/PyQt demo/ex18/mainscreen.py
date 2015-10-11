from PyQt4 import QtCore, QtGui
from window_main import Ui_MainWindow

class mainscreen(QtGui.QMainWindow, Ui_MainWindow):
        def __init__(self, parent=None):
                super(mainscreen,self).__init__(parent)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)