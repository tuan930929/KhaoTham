from PyQt4 import QtCore, QtGui
from window_main import Ui_MainWindow
from currency import Ui_CurrencyWindow

class CurrencyWindow(QtGui.QMainWindow, Ui_CurrencyWindow):
    def __init__(self, parent=None):
        super(CurrencyWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)

class MainScreen(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        self.currencyButton.clicked.connect(self.handleCurrencyButton)

    def handleCurrencyButton(self):
        window = CurrencyWindow(self)
        window.show()