def rodCuttingBottomUp(prices, length):
    dp = [0] * (length + 1)

    # check all possible rod lengths
    for i in range(1, length + 1):
        maxRevenue = -1
        # make a cut at each step
        for j in range(1, i + 1):
            maxRevenue = max(maxRevenue, prices[j] + dp[i - j])
        dp[i] = maxRevenue

    return dp[length]


def rodCuttingTopDown(prices, length):
    # init memo
    revenues = [-1] * (length + 1)
    return _rodCuttingTopDown(prices, length, revenues)


def _rodCuttingTopDown(prices, length, revenues):
    if revenues[length] != -1:
        return revenues[length]

    if length == 0:
        maxRevenue = 0
    else:
        maxRevenue = -1
        for i in range(1, length + 1):
            maxRevenue = max(
                maxRevenue, prices[i] + _rodCuttingTopDown(prices, length - i, revenues)
            )
    revenues[length] = maxRevenue

    return revenues[length]


# Price for rods of length 0 to 10
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

max_rev_bottom_up = [
    rodCuttingBottomUp(prices, length) for length in range(len(prices))
]
print(f"Bottom up = {max_rev_bottom_up}")

max_rev_top_down = [rodCuttingTopDown(prices, length) for length in range(len(prices))]
print(f"Top down = {max_rev_top_down}")
