def lengthOfLIS(nums) -> int:
    # two lists to store the subsequences at each step and their lengths so to not compute them again
    subsequences = [[nums[i]] for i in range(len(nums))]
    lengths = [1 for _ in range(len(nums))]
    # break the array into smaller subarrays
    for j in range(len(nums)):
        # iterate over every subarray
        for i in range(j + 1):
            # check if element at j can be added into the subsequences
            if nums[j] > nums[i]:
                # check if it's feasible adding the element
                if lengths[i] + 1 > lengths[j]:
                    lengths[j] = lengths[i] + 1
                    subsequences[j] = subsequences[i] + [nums[j]]

    return lengths[-1]


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))
