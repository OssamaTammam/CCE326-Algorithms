def mergeSort(arr):
    # base case
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    mergeSort(leftArr)
    mergeSort(rightArr)

    merge(arr, leftArr, rightArr)


def merge(arr, leftArr, rightArr):
    i = j = k = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] > rightArr[j]:
            arr[k] = rightArr[j]
            j += 1
        else:
            arr[k] = leftArr[i]
            i += 1
        k += 1

    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1


arr = [6, 7, 2, 1, -1, 0, 4]
mergeSort(arr)
print(arr)
