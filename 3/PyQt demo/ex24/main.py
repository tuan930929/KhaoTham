from PyQt4 import QtGui
from mainscreen import mainscreen

def main():
    import sys
    qApp = QtGui.QApplication(sys.argv)
    aw = mainscreen()
    aw.show()
    sys.exit(qApp.exec_())

if __name__ == '__main__':
    main()