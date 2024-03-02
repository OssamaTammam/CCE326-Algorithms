def betterBinarySearch(arr, low, high, key):
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
