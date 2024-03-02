def maxCrossingSubArray(arr, low, mid, high):
    leftSum = -1e6
    sum = 0
    maxLeft = mid
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    rightSum = -1e6
    sum = 0
    maxRight = mid + 1
    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > rightSum:
            rightSum = sum
            maxRight = i

    return (maxLeft, maxRight, leftSum + rightSum)


def maxSubArray(arr, low, high):
    if high == low:
        return (low, high, arr[low])
    else:
        mid = (high + low) // 2

        (leftLow, leftHigh, leftSum) = maxSubArray(arr, low, mid)
        (rightLow, rightHigh, rightSum) = maxSubArray(arr, mid + 1, high)
        (crossLow, crossHigh, crossSum) = maxCrossingSubArray(arr, low, mid, high)

    maxSum = max(leftSum, rightSum, crossSum)
    if maxSum == leftSum:
        return leftLow, leftHigh, leftSum
    elif maxSum == rightSum:
        return rightLow, rightHigh, rightSum
    else:
        return crossLow, crossHigh, crossSum


arr = [2, 3, 4, 5, 7]
n = len(arr)

max_sum = maxSubArray(arr, 0, n - 1)
print("(Low, High, Sum): ", max_sum)
