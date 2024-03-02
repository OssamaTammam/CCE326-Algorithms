def binarySearch(arr, low, high, key):
    mid = (low + high) // 2

    if low > high:
        return -1

    if key == arr[mid]:
        return mid

    if key < arr[mid]:
        return binarySearch(arr, low, mid, key)
    else:
        return binarySearch(arr, mid + 1, high, key)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sol = binarySearch(arr, 0, len(arr) - 1, 3)
print(sol)
