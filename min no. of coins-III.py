def coinmin(coins,target):
    dp = [float("inf")]*(target+1)
    dp[0]=0

    for coin in  coins:
        for val in range(coin,target+1):
            dp[val] = min(dp[val],dp[val-coin]+1)
    return dp[target]

coins=[1,2,5]
target=11
print(coinmin(coins,target))