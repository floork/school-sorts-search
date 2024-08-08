import sorting
import searching

from PyQt6 import QtWidgets, uic
import sys
import random

def getRandList(amount: int, min: int = -sys.maxsize - 1, max: int = sys.maxsize):
    return [random.randint(min, max) for _ in range(amount)]

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent= None ) -> None:
        super(MainWindow, self).__init__(parent)
        uic.load_ui("window.ui", self)

        self._unsorted_list_obj = self.ls_unsorted
        self._sorted_list_obj = self.ls_sorted   
        self._stats_obj = self.lbl_stats
        self._input_obj = self.sp_input
        self._ascending_obj = self.direction
        self._search_input_obj = self.le_search_input
        self._search_output_obj = self.lbl_search_output

        self._unsorted_list = getRandList(self._input_obj.value())
        self.ls_unsorted.addItems([str(num) for num in self._unsorted_list])

    def genRandom(self):
        self._unsorted_list = getRandList(self._input_obj.value())
        
        self._unsorted_list_obj.clear()
        self._unsorted_list_obj.addItems([str(num) for num in self._unsorted_list])

        self._sorted_list_obj.clear()

    def def_sort(self):
        sorted_list = self._unsorted_list
        sorted_list.sort()

        self._sorted_list_obj.clear()
        self._sorted_list_obj.addItems([str(num) for num in sorted_list])

    def bubble_sort(self):
        sorted_list = sorting.bubble_sort(self._unsorted_list)

        self._sorted_list_obj.clear()
        self._sorted_list_obj.addItems([str(num) for num in sorted_list])

    def quick_sort(self):
        sorted_list = sorting.quick_sort(self._unsorted_list)

        self._sorted_list_obj.clear()
        self._sorted_list_obj.addItems([str(num) for num in sorted_list])

    def selection_sort(self):
        sorted_list = sorting.selection_sort(self._unsorted_list)

        self._sorted_list_obj.clear()
        self._sorted_list_obj.addItems([str(num) for num in sorted_list])

    def merge_sort(self):
        sorted_list = sorting.merge_sort(self._unsorted_list)

        self._sorted_list_obj.clear()
        self._sorted_list_obj.addItems([str(num) for num in sorted_list])

    def linear_search(self):
        inp = self._search_input_obj.text()

        try:
            index = searching.linearSearch(self._unsorted_list,inp)
        except KeyError as e: 
            index = f"{e}"

        self._search_output_obj.setText(index)

    def binary_search(self):
        inp = self._search_input_obj.text()
        
        try:
            index = searching.binary_search(self._unsorted_list,inp)
        except KeyError as e: 
            index = f"{e}"

        self._search_output_obj.setText(index)
        
