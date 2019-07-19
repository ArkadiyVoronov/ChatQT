import sys
from PyQt5 import QtWidgets
from main_window import MainWindow

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())