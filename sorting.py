def bubble_sort(arr):
  
  # Outer loop to iterate through the list n times
  for n in range(len(arr) - 1, 0, -1):
    
    swapped = False
    
    # Inner loop to compare adjacent elements
    for i in range(n):
      if arr[i] > arr[i + 1]:
        
        # Swap elements if they are in the wrong order
        swapped = True
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
      
      # If we didn't make any swaps in a pass, 
      # the list is already sorted and we can 
      # exit the outer loop
      if not swapped:
        return

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

# Function to merge two sorted arrays
def merge(arr1, arr2):
    i = 0
    j = 0
    # Array to store the merged sorted array
    result = []
    while(i < len(arr1) and j < len(arr2)):
        # If arr1[i] is smaller than arr2[j], push arr1[i] into the result and move to the next element in arr1
        if arr2[j] > arr1[i]:
            result.append(arr1[i])
            i += 1
        # If arr2[j] is smaller than arr1[i], push arr2[j] into the result and move to the next element in arr2
        else:
            result.append(arr2[j])
            j += 1

    # Push the remaining elements of arr1, if any
    while(i < len(arr1)):
        result.append(arr1[i])
        i += 1
        # Push the remaining elements of arr2, if any
    while(j < len(arr2)):
        result.append(arr2[j])
        j += 1

    return result


# Function to sort arr using merge sort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    # Sort the left half
    left = mergeSort(arr[:mid])
    # Sort the right half
    right = mergeSort(arr[mid:])

    return merge(left, right)
