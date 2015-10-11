import sys, random
from PyQt4 import QtCore, QtGui

class TabContainer(QtGui.QWidget):
  def __init__(self):
    super(TabContainer, self).__init__()
    self.next_item_is_table = False
    self.initUI()

  def initUI(self):
    self.setGeometry( 150, 150, 650, 350)
    self.tabwidget = QtGui.QTabWidget(self)
    vbox = QtGui.QVBoxLayout()
    vbox.addWidget(self.tabwidget)
    self.setLayout(vbox)
    self.pages = []
    self.add_page()
    self.show()

  def create_page(self, *contents):
    page = QtGui.QWidget()
    vbox = QtGui.QVBoxLayout()
    for c in contents:
        vbox.addWidget(c)

    page.setLayout(vbox)
    return page

  def create_table(self):
    rows, columns = random.randint(2,5), random.randint(1,5)
    table = QtGui.QTableWidget( rows, columns )
    for r in xrange(rows):
        for c in xrange(columns):
            table.setItem( r, c, QtGui.QTableWidgetItem( str( random.randint(0,10) ) ) )
    return table

  def create_list(self):
    list = QtGui.QListWidget()
    columns = random.randint(2,5)
    for c in xrange(columns):
        QtGui.QListWidgetItem( str( random.randint(0,10) ), list )

    return list

  def create_new_page_button(self):
    btn = QtGui.QPushButton('Create a new page!')
    btn.clicked.connect(self.add_page)
    return btn

  def add_page(self):
    if self.next_item_is_table:
        self.pages.append( self.create_page( self.create_table(), self.create_new_page_button() ) )
        self.next_item_is_table = False
    else:
        self.pages.append( self.create_page( self.create_list(), self.create_new_page_button() ) )
        self.next_item_is_table = True

    self.tabwidget.addTab( self.pages[-1] , 'Page %s' % len(self.pages) )
    self.tabwidget.setCurrentIndex( len(self.pages)-1 )

app = QtGui.QApplication(sys.argv)
ex = TabContainer()
sys.exit(app.exec_())