import math


def coinChange(coins, targetValue):
    dp = [math.inf] * (targetValue+1)
    dp[0] = 0
    for currentTargetValue in range(1, targetValue+1):
        for coin in coins:
            if currentTargetValue - coin >= 0:
                dp[currentTargetValue] = min(
                    dp[currentTargetValue], 1 + dp[currentTargetValue - coin])
    return dp[targetValue] if dp[targetValue] != math.inf else -1


coins = [1, 3, 4]
targetValue = 15
print(f"Minimum number of coins: {coinChange(coins,targetValue)}")
