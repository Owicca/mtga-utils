from mtga.set_data import all_mtga_cards

from PyQt5.QtWidgets import QMessageBox, QPushButton, \
QVBoxLayout
from PyQt5.QtGui import QStandardItem

import mtga_export as mtga


class MtgaModel(mtga.MtgaLog):

	@staticmethod
	def loadData(data, model):

		model.clear()
		for card in data:
			model.appendRow(QStandardItem(str(card)))


	def execute_export():

		popup = QMessageBox()

		popup.setText("Are you sure?")
		popup.setStandardButtons([QMessageBox.StandardButton.Ok,
			QMessageBox.StandardButton.Cancel])

		if popup:
			print('executed')
		else:
			print('making sure settings are allright')