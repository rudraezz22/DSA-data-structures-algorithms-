def wordbreak(s,word_break):
    n=len(s)
    dp=[False]*(n+1)
    dp[0]=True

    for i in range(1,n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_break:
                dp[i]=True
                break
    return dp[n]

str1="BlackChocolate"
word_break=["white","Chocolate"]

if  wordbreak(str1,word_break):
    print("String can be segmented")
else:
    print("string can't be segmented")

