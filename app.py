import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout

from PyQt5.QtWidgets import QWidget, QPushButton, \
QToolTip, QLabel, QComboBox, QTextEdit, \
QScrollArea, QSizePolicy, QListView

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QStandardItemModel

import datetime
import utils as ut
import MtgaModel as Model


class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.res_card = []

		self.initLayout()

	def initLayout(self):

		self.resize(500, 500)
		self.setWindowTitle('MTGA Arena Deck Export')
		mw = QWidget(self)
		mw.resize(500, 500)
		self.initComponents(mw)
		self.statusBar().showMessage("v " + Model.mtga.__version__)
		self.show()

	def initComponents(self, mw):

		layout = QVBoxLayout(mw)

		mod = Model.MtgaModel(Model.mtga.MTGA_WINDOWS_LOG_FILE)
		for card, count in mod.get_collection():
			#self.res_text += "{1} {2} {3}".format(card.mtga_id, str(card) + "\n", count)
			self.res_card.append(card)

		format_dropdown = QComboBox()
		format_dropdown.addItem("Goldfish")
		format_dropdown.addItem("Deckstats")

		annoying_label = QLabel("Export in")
		annoying_label2 = QLabel("format")

		execute = QPushButton('Execute')

		layout.addWidget(annoying_label)
		layout.addWidget(format_dropdown)
		layout.addWidget(annoying_label2)

		results_list = QListView()
		results_list_mod = QStandardItemModel(results_list)
		mod.loadData(self.res_card, results_list_mod)

		results_list.setModel(results_list_mod)

		layout.addWidget(results_list)
		layout.addWidget(execute)

		execute.clicked.connect(mod.execute_export)

	def keyPressEvent(self, e):
		"""
		TODO: Remove this on prod
		Developing in a tilting window linux
		"""

		if e.key() == Qt.Key_Escape:
			self.close()



if __name__ == '__main__':

	app = QApplication(sys.argv)
	win = App()
	sys.exit(app.exec_())