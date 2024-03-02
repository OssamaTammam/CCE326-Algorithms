from random import randint


def quickSort(arr):
    _quickSort(arr, 0, len(arr) - 1)


def _quickSort(arr, low, high):
    # base case
    if low >= high:
        return

    pivot = partition(arr, low, high)
    _quickSort(arr, low, pivot)
    _quickSort(arr, pivot + 1, high)


def partition(arr, low, high):
    # choose a random pivot
    pivot = randint(low, high)
    # move that pivot to the end of the array
    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivotElement = arr[high]

    # pointer that keeps track of where lesser elements should go one by one from the start of the array
    i = low - 1
    # high because we don't want to iterate over our pivot
    for j in range(low, high):
        if arr[j] < pivotElement:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    # i should be at the position for the last lesser element encountered so normally the pivot should be the next position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


arr = [3, 6, -1, -5, 6, 7, 1, 2, 0]
quickSort(arr)
print(f"Sorted Array: {arr}")
