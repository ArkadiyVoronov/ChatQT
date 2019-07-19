from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
	def __init__(parent=None):
		super(MainWindow, self).__init__(parent)

		text_edit = QtWidgets.QTextEdit(self)
        #text_edit.setReadOnly(True)

        self.setCentralWidget(text_edit)