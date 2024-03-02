def maxElement(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    leftMax = maxElement(arr, low, mid)
    rightMax = maxElement(arr, mid + 1, high)

    return max(leftMax, rightMax)


arr = [1, 6, 4, 100, 3, 5, 6, 7]
print(maxElement(arr, 0, len(arr) - 1))
