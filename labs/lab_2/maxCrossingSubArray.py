import math


def maxCrossingSubArray(arr, low, high):
    # base case
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    sumLeft = maxCrossingSubArray(arr, low, mid)
    sumRight = maxCrossingSubArray(arr, mid + 1, high)
    sumCrossing = crossing(arr, low, high, mid)

    return max(sumLeft, sumRight, sumCrossing)


def crossing(arr, low, high, mid):
    # max crossing left
    maxLeft = -math.inf
    curr = 0
    for i in range(mid, low - 1, -1):
        curr += arr[i]
        maxLeft = max(maxLeft, curr)

    # max crossing right
    maxRight = -math.inf
    curr = 0
    for i in range(mid + 1, high + 1):
        curr += arr[i]
        maxRight = max(maxRight, curr)

    return maxRight + maxLeft
