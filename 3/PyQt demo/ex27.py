import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        action = QtGui.QAction(QtGui.QIcon('action.png'), '&New Window', self)
        action.triggered.connect(self.new_win)
        self.menuBar().addMenu('&File').addAction(action)
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def new_win(self):
        name, ok = QtGui.QInputDialog.getText(self, 'Input', 'Enter name:')
        print name, ok

app = QtGui.QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec_())