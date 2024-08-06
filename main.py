import sys
from ui import MainWindow

from PyQt6 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
