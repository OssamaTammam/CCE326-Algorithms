from random import randint


def kthLargestElement(nums, low, high, k):
    target = len(nums) - k
    pivotIndex = partition(nums, low, high)

    if pivotIndex == target:
        return nums[pivotIndex]
    elif pivotIndex > target:
        return kthLargestElement(nums, low, pivotIndex - 1, k)
    else:
        return kthLargestElement(nums, pivotIndex + 1, high, k)


def partition(nums, low, high):
    pivotIndex = randint(low, high)
    nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]
    pivot = nums[high]

    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    return i + 1


nums = [3, 2, 1, 7, 5, 4]
print(kthLargestElement(nums, 0, len(nums) - 1, 2))
