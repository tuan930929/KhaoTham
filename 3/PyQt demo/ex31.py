import sys
from PyQt4 import QtGui

class MyAppMainWindow(QtGui.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        #same as self.connect(self.pushButton, SIGNAL('clicked'),self.openDialog) but more Pythonic.
        self.pushButton.connect(self.openDialog) 
        
    def openDialog(self):
        self.dlg = MyAppDialog()
        self.dlg.show()
        
    
class MyAppDialog(QtGui.QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.connect(self.close)
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = MyAppMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())