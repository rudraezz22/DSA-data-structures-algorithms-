def recursive_factorial(n):
    if n==0:
        return 1

    return n*recursive_factorial(n-1)

n=5
result = recursive_factorial(n)
print(f"the factorial of {n} is : {result} ")

#using DP
def DP_factorial(n):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1,n+1):
        dp[i] = i * dp[i-1]

    return dp[n]

n = 5
result1=DP_factorial(n)
print(f"the factorial of {n} is: {DP_factorial(n)} ")


