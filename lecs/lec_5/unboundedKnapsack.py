def unboundedKnapsack(weights, values, maxWeight):
    # dp table of weights
    n = len(weights)
    dp = [0] * (maxWeight + 1)

    # iterate over all possible weights of the knapsack
    for i in range(1, maxWeight + 1):
        maxValue = 0
        for j in range(n):
            if i - weights[j] >= 0:
                maxValue = max(maxValue, values[j] + dp[i - weights[j]])
        dp[i] = maxValue

    return dp[maxWeight]


# Driver program
maxWeight = 100
values = [10, 30, 20]
weights = [5, 10, 15]
print(f"Maximum value : {unboundedKnapsack(weights,values,maxWeight)}")
