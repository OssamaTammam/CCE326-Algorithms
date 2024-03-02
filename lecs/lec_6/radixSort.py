def countingSort(arr, digitPlace):
    # to get the certain digit needed from the num ex: if the number is 345 to get the first digit %10^1
    n = len(arr)
    exp = 10**digitPlace
    count = [0] * 10
    output = [0] * n

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    return output


def radixSort(arr):
    n = len(arr)
    maxSigDigit = 0
    for i in range(n):
        currSigDigit = 0
        num = arr[i]
        while num > 0:
            num = num // 10
            currSigDigit += 1
        maxSigDigit = max(maxSigDigit, currSigDigit)

    for currDigit in range(maxSigDigit):
        arr = countingSort(arr, currDigit)

    return arr


arr = [356, 321, 777, 59]
arr = radixSort(arr)
print(arr)
