#using dp
def distchange(str1,str2):
    m=len(str1)
    n=len(str2)

    dp=[[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0]=i

    for j in range(n+1):
        dp[0][j]=j

    for i in range(1,m+1):
        for j in range(n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]

str1="saturday"
str2="sunday"
print(distchange(str1,str2))


#using recursion
def distrecur(str1,str2,m,n):
    

    if m==0:
        return n
    if n==0:
        return m

    if str1[m-1]==str2[n-1]:
        return distrecur(str1,str2,m-1,n-1)

    return 1+min(distrecur(str1,str2,m-1,n),
                 distrecur(str1,str2,m,n-1),
                 distrecur(str1,str2,m-1,n-1))

str1="saturday"
str2="sunday"
print(distrecur(str1,str2,len(str1),len(str2)))
    
    