def knapsack(nums, sum):
    n = len(nums)  # how many elements do we have
    # table init to zero to store each subproblem
    dp = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]

    for item in range(1, n + 1):
        for weight in range(1, sum + 1):
            notTake = dp[item - 1][weight]
            take = 0
            if nums[item - 1] <= weight:
                take = nums[item - 1] + dp[item - 1][(weight - nums[item - 1])]
            dp[item][weight] = max(take, notTake)

    for i in range(n + 1):
        if dp[i][sum] == sum:
            return True

    return False


nums = [1, 2, 6]
target = 3
print(knapsack(nums, target))
