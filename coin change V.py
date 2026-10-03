def coinchange(coins,amount):
    dp= [float("inf")]*(amount+1)
    dp[0]=0

    for i in range(1,amount+1):
        for coin in coins:
            if coin<=i:
               dp[i]=min(dp[i],dp[i-coin]+1)
    if dp[amount]==float("inf"):
        return -1
    else:
        return dp[amount]

coins = [3,2,10]
amount=12
print("the min no. of coins are :" , coinchange(coins,amount))



#using recursion

def coinchange1(coins,n,sum):
    if (sum==0):
        return 1
    if (sum<=0):
        return 0
    if n<=0:
        return 0

    return coinchange1(coins,n-1,sum) + coinchange1(coins,n,sum-coins[n-1])

coins = [1,2]
n = len(coins)
sum =3
print(coinchange1(coins,n,sum))
