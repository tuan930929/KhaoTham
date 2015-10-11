from PyQt4 import QtGui, QtCore

class MyWindow(QtGui.QDialog):    # any super class is okay
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.button = QtGui.QPushButton('Press')
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.button)
        self.setFixedSize(500,500)
        self.move(600,100)
        self.setLayout(layout)
        self.button.clicked.connect(self.create_child)
    def create_child(self):
        # here put the code that creates the new window and shows it.
        child = MainScreen()
        child.show()

class MainScreen(QtGui.QDialog):
    
    def __init__(self):
        super(MainScreen, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        trainingButton = QtGui.QPushButton("Training")
        # trainingButton.clicked.connect(self.training)
        detectButton = QtGui.QPushButton("Detect")
        # detectButton.clicked.connect(self.detect)

        picture = QtGui.QLabel(self)
        picture.move(15, 10)
        pixmap = QtGui.QPixmap("ex30-timekeeper.png")
        pixmap1 = pixmap.scaled(480, 450)
        picture.setPixmap(pixmap1)
        picture.show()

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(trainingButton)
        hbox.addWidget(detectButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setFixedSize(500,500)
        self.move(600,100)
        self.setWindowTitle('Timekeeper by Face Application')    
        self.show()
        app.exit(self.exec_())

    def training(self):
        trainingScreen = TrainingScreen()
        trainingScreen.show()
        # return trainingScreen

    def detect(self):
        detectScreen = DetectScreen()
        trainingScreen.show()
        return trainingScreen

    # def closeEvent(self, event):
        
    #     reply = QtGui.QMessageBox.question(self, 'Message',
    #         "Are you sure to quit?", QtGui.QMessageBox.Yes | 
    #         QtGui.QMessageBox.No, QtGui.QMessageBox.No)

    #     if reply == QtGui.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore() 




if __name__ == '__main__':
    # QApplication created only here.
    app = QtGui.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()