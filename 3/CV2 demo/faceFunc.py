import cv2
import numpy as np
from PyQt4 import QtGui, QtCore
from dialogCapture import DialogCapture

class Capture():
    def __init__(self):
        self.capturing = False
        self.cascPath = "haarcascades/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.c = cv2.VideoCapture(0)

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