import sys
from PyQt4 import QtCore, QtGui

class mainscreen(QtGui.QMainWindow):
        def __init__(self, parent=None):
            super(mainscreen,self).__init__(parent)

            self.button = QtGui.QPushButton("push")
            self.button.clicked.connect(self.pushed)

        @pyqtSlot()
        def pushed(self):
            # in this section here you can create the new window and show it


 qApp = QtGui.QApplication(sys.argv)
    aw = mainscreen()
    aw.show()
    sys.exit(qApp.exec_())