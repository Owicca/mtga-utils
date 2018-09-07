def previewDispatch(self, data):

		default = QDate(datetime.datetime.now())

		self.statusBar().showMessage(str(default) + ' | ' + data)