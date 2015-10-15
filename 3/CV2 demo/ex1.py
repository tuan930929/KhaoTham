import cv2
import numpy as np
from PIL import Image
from PyQt4 import QtGui, QtCore
# from faceFunc import Capture

class Capture():
    def __init__(self):
        self.capturing = False
        self.cascPath = "haarcascades/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        recognizer = cv2.createLBPHFaceRecognizer()
        # self.c = cv2.VideoCapture(0)

    def startCapture(self):
        print "pressed start"
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

    def get_image(self):
         retval, im = self.c.read()
         return im

    def captureFace(self):
        dialog = DialogCapture()
        text = dialog.face()
        for i in xrange(30):
            temp = self.get_image()
        print("Taking image...")
        camera_capture = self.get_image()
        file = "images/" + text + ".png"
        print(file)
        cv2.imwrite(str(file), camera_capture)
        # print "pressed Capture Face"
        # text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
        #     'Enter image face name:')
        
        # if ok:
        #     print "image face name: " + text

    def trainingFace(self):
        print "pressed Training Face"

    def recognizeFace(self):
        print "pressed Recognize Face"

    def endCapture(self):
        print "pressed End"
        self.capturing = False
        # cv2.destroyAllWindows()

    def quitCapture(self):
        print "pressed Quit"
        cap = self.c
        cv2.destroyAllWindows()
        cap.release()
        QtCore.QCoreApplication.quit()

class Window(QtGui.QWidget):
    def __init__(self):

        # c = cv2.VideoCapture(0)

        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()
        self.start_button = QtGui.QPushButton('Start',self)
        self.start_button.clicked.connect(self.capture.startCapture)

        self.capture_face = QtGui.QPushButton('Capture Face',self)
        self.capture_face.clicked.connect(self.capture.captureFace)

        self.training_face = QtGui.QPushButton('Training Face',self)
        self.training_face.clicked.connect(self.capture.trainingFace)

        self.recognize_face = QtGui.QPushButton('Recognize Face',self)
        self.recognize_face.clicked.connect(self.capture.recognizeFace)

        self.end_button = QtGui.QPushButton('End',self)
        self.end_button.clicked.connect(self.capture.endCapture)

        self.quit_button = QtGui.QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.capture.quitCapture)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.capture_face)
        vbox.addWidget(self.training_face)
        vbox.addWidget(self.recognize_face)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(200,200,300,300)
        self.show()


class DialogCapture(QtGui.QInputDialog):
    def __init__(self):

        # c = cv2.VideoCapture(0)

        QtGui.QInputDialog.__init__(self)

    def face(self):
        print "pressed Capture Face"
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter image face name:')
        
        if ok:
            print "image face name: " + text
            return text

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())