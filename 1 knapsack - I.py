def knapsack(weight,values,capacity):
    n=len(weight)

    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weight[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],values[i-1]+dp[i-1][j-weight[i-1]])
            else:
                dp[i][j]=dp[i-1][j]

    max1 = dp[n][capacity]

    item_knapsack = []
    j = capacity
    for x in range(n,0,-1):
        if dp[x][j]!=dp[x-1][j]:
            item_knapsack.append(x-1)
            j-=weight[x-1]
    return max1 , item_knapsack[::-1]

weight = [2,3,4,5]
values=[3,4,5,6]
capacity=5

maxvalue,items=knapsack(weight,values,capacity)
print(maxvalue,items)


#subset prob

def subset1(subset,target_sum):
    n=len(subset)

    dp=[[False for _ in range(target_sum+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0]=True
    for i in range(n+1):
        for j in range(target_sum+1):
            if subset[i-1]<=j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-subset[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][target_sum]

subset = [3,34,4,12,5,2]
target_sum=9
if subset1(subset,target_sum):
    print("yes")
else:
    print("no")