def indexSearch(arr, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        indexSearch(arr, low, mid)
    else:
        indexSearch(arr, mid + 1, high)
