from typing import List

def linearSearch(arr: List[int], x: int) -> int:
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    raise KeyError(f'Element {x} not found in array')

def binary_search(arr: List[int], x: int) -> int:
    def binary_search_recursive(arr: List[int], low: int, high: int, x: int) -> int:
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary_search_recursive(arr, low, mid - 1, x)
            else:
                return binary_search_recursive(arr, mid + 1, high, x)
        else:
            return -1
    
    result = binary_search_recursive(arr, 0, len(arr) - 1, x)
    if result == -1:
        raise KeyError(f'Element {x} not found in array')
    return result
