from random import randint


# generate a random array with variable sized of integers between 0 and 1000
def generateRandomArray(size):
    return [randint(0, 1000) for _ in range(size)]


def quickSelect(arr, k):
    return _quickSelect(arr, k, 0, len(arr) - 1)


def _quickSelect(arr, k, low, high):
    # base case if there is only element
    if low == high:
        return arr[low]

    pivot = partition(arr, low, high)
    rank = pivot - low + 1

    if rank == k:
        return arr[rank]
    elif k < rank:
        return _quickSelect(arr, k, low, pivot - 1)
    else:
        return _quickSelect(arr, k, pivot + 1, high)


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


arr = generateRandomArray(10)
k = 5
ans = quickSelect(arr, k)
print(f"Array is {arr}\nSorted is {sorted(arr)}")
print(f"The {k}th smallest element is {ans}")
