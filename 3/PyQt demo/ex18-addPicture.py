import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)

label = QLabel()
pixmap = QPixmap("ex18-timekeeper.png")
label.setPixmap(pixmap)
label.show()

sys.exit(app.exec_())