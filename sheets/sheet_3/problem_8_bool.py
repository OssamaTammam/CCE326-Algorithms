def knapsack(nums, sum):
    n = len(nums)  # how many elements do we have
    # table init to zero to store each subproblem
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for item in range(1, n + 1):
        for weight in range(1, sum + 1):
            if nums[item - 1] <= weight:
                take = dp[item - 1][weight - nums[item - 1]]
            notTake = dp[item - 1][weight]

            dp[item][weight] = take or notTake

    return dp[n][sum]


nums = [1, 2, 3]
target = 4
print(knapsack(nums, target))
