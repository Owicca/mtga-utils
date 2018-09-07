from PyQt5.QtWidgets import QMessageBox, QPushButton


def execute_export():

	popup = QMessageBox()

	popup.setText("Are you sure?")
	popup.setStandardButtons([QMessageBox.StandardButton.Ok,
		QMessageBox.StandardButton.Cancel])

	if popup:
		print('executed')
	else:
		print('making sure settings are allright')