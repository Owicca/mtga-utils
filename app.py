import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout
from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QLabel
from PyQt5.QtCore import QDate
import datetime
import actions as a


class App(QMainWindow):

	def __init__(self):
		super().__init__()

		self.initLayout()

	def initLayout(self):

		self.resize(500, 500)
		self.setWindowTitle('MTGA Arena Deck Export')
		mw = QWidget(self)
		mw.resize(500, 500)
		self.initComponents(mw)
		self.show()

	def initComponents(self, mw):

		layout = QFormLayout(mw)
		execute = QPushButton('Execute', self)

		layout.addWidget(execute)

		execute.clicked.connect(a.execute_export)

	def previewDispatch(self, data):

		default = QDate(datetime.datetime.now())

		self.statusBar().showMessage(str(default) + ' | ' + data)

	def execute(self):
		print('executed')



if __name__ == '__main__':

	app = QApplication(sys.argv)
	win = App()
	sys.exit(app.exec_())