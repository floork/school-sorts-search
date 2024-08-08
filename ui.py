import time

import sorting
import searching

from PyQt6 import QtWidgets, uic
import sys
import random

def getRandList(amount: int, min: int = -10000, max: int = 10000):
    return [random.randint(min, max) for _ in range(amount)]


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent= None ) -> None:
        super(MainWindow, self).__init__(parent)
        uic.loadUi("window.ui", self)

        self._unsorted_list_obj = self.ls_unsorted
        self._sorted_list_obj = self.ls_sorted
        self._stats_obj = self.lbl_stats
        self._input_obj = self.sp_input
        self._ascending_obj = self.cb_direciton
        self._search_input_obj = self.le_serach_input
        self._search_output_obj = self.lbl_search_output

        self._unsorted_list = getRandList(self._input_obj.value())
        self._sorted_list = []
        self.ls_unsorted.addItems([str(num) for num in self._unsorted_list])

        self._took_time_sort = 0

    def get_random(self):
        self._unsorted_list = getRandList(self._input_obj.value())

        self._unsorted_list_obj.clear()
        self._unsorted_list_obj.addItems([str(num) for num in self._unsorted_list])

        self._sorted_list_obj.clear()

    def show_stats(self):
        if len(self._unsorted_list) == 0:
            return
        field_count = self._input_obj.value()
        sum_list = sum(self._unsorted_list)
        max_list = max(self._unsorted_list)
        min_list = min(self._unsorted_list)
        avg_list = sum_list / field_count

        self._stats_obj.setText(f"Field count: {field_count} \nSum: {sum_list} \nMax: {max_list} \nMin: {min_list} \nAvg: {avg_list} \nTook: {self._took_time_sort}s")

    def def_sort(self):
        start_time = time.time()
        sorted_list = self._unsorted_list
        sorted_list.sort()
        self._took_time_sort = time.time() - start_time

        self._sorted_list_obj.clear()
        self._sorted_list = [str(num) for num in sorted_list]
        if not self._ascending_obj.isChecked():
            self._sorted_list_obj.addItems(reversed(self._sorted_list))
            return
        self._sorted_list_obj.addItems(self._sorted_list)
        self.show_stats()

    def bubble_sort(self):
        start_time = time.time()
        sorted_list = sorting.bubble_sort(self._unsorted_list)
        self._took_time_sort = time.time() - start_time

        self._sorted_list_obj.clear()
        self._sorted_list = [str(num) for num in sorted_list]
        if not self._ascending_obj.isChecked():
            self._sorted_list_obj.addItems(reversed(self._sorted_list))
            return
        self._sorted_list_obj.addItems(self._sorted_list)
        self.show_stats()

    def quick_sort(self):
        start_time = time.time()
        sorted_list = sorting.quick_sort(self._unsorted_list)
        self._took_time_sort = time.time() - start_time

        self._sorted_list_obj.clear()
        self._sorted_list = [str(num) for num in sorted_list]
        if not self._ascending_obj.isChecked():
            self._sorted_list_obj.addItems(reversed(self._sorted_list))
            return
        self._sorted_list_obj.addItems(self._sorted_list)
        self.show_stats()

    def selection_sort(self):
        start_time = time.time()
        sorted_list = sorting.selection_sort(self._unsorted_list)
        self._took_time_sort = time.time() - start_time

        self._sorted_list_obj.clear()
        self._sorted_list = [str(num) for num in sorted_list]
        if not self._ascending_obj.isChecked():
            self._sorted_list_obj.addItems(reversed(self._sorted_list))
            return
        self._sorted_list_obj.addItems(self._sorted_list)
        self.show_stats()

    def merge_sort(self):
        start_time = time.time()
        sorted_list = sorting.merge_sort(self._unsorted_list)
        self._took_time_sort = time.time() - start_time

        self._sorted_list_obj.clear()
        self._sorted_list = [str(num) for num in sorted_list]
        if not self._ascending_obj.isChecked():
            self._sorted_list_obj.addItems(reversed(self._sorted_list))
            return
        self._sorted_list_obj.addItems(self._sorted_list)
        self.show_stats()

    def linear_search(self):
        start_time = time.time()
        inp = self._search_input_obj.text()
        took = time.time() - start_time

        try:
            index = f"index found at: {searching.linearSearch(self._sorted_list, inp)} in sorted list it took {took}s"
        except KeyError as e:
            index = f"{e}"

        self._search_output_obj.setText(index)

    def binary_search(self):
        start_time = time.time()
        inp = self._search_input_obj.text()
        took = time.time() - start_time

        try:
            index = f"index found at: {searching.linearSearch(self._sorted_list, inp)} in sorted list it took {took}s"
        except KeyError as e:
            index = f"{e}"

        self._search_output_obj.setText(index)

