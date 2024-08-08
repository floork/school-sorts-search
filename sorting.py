from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not swapped:
            break
    return arr

def selection_sort(array: List[int]) -> List[int]:
    size = len(array)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]
    return array

def partition(array: List[int], low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def _quick_sort(array: List[int], low: int, high: int):
    if low < high:
        pi = partition(array, low, high)
        _quick_sort(array, low, pi - 1)
        _quick_sort(array, pi + 1, high)

def quick_sort(array: List[int]) -> List[int]:
    _quick_sort(array, 0, len(array) - 1)
    return array

def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr2[j] > arr1[i]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
