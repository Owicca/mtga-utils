import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout
from PyQt5.QtWidgets import QWidget, QPushButton, \
QToolTip, QLabel, QComboBox, QTextEdit, \
QScrollArea
from PyQt5.QtCore import QDate, Qt
import datetime
import actions as acc
import utils as ut
import mtga_export.MtgaLog as Mtga


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

		layout = QVBoxLayout(mw)

		format_dropdown = QComboBox()
		format_dropdown.addItem("Goldfish")
		format_dropdown.addItem("Deckstats")

		annoying_label = QLabel("Export in")
		annoying_label2 = QLabel("format")
		results_textarea = QScrollArea()
		res_text_data = QLabel("Preview\n", results_textarea)
		results_textarea.ensureVisible(150, 150, 0, 0)

		execute = QPushButton('Execute')

		layout.addWidget(annoying_label)
		layout.addWidget(format_dropdown)
		layout.addWidget(annoying_label2)

		layout.addWidget(results_textarea)

		layout.addWidget(execute)

		execute.clicked.connect(acc.execute_export)

	def keyPressEvent(self, e):
		"""
		Developing in a tilting window linux
		TODO: Remove this on prod
		"""

		if e.key() == Qt.Key_Escape:
			self.close()

	def execute(self):
		print('executed')



if __name__ == '__main__':

	app = QApplication(sys.argv)
	win = App()
	sys.exit(app.exec_())