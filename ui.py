import sorting
import searching

from PyQt6 import QtWidgets, uic

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent= None ) -> None:
        super(MainWindow, self).__init__(parent)
        uic.load_ui("window.ui", self)

    def bubble_sort(self):
        ...

    def quick_sort(self):
        ...

    def def_sort(self):
        ...

    def selection_sort(self):
        ...

    def binary_search(self):
        ...

    def linear_searc(self):
        ...
