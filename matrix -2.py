x = [[8,4,1]
     ,[5,6,3],
     [77,21,32]]
ans = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        ans[i][j] = x[j][i]

for p in ans:
    print(p)


#sum of columns:
y = [[8,4,1]
     ,[5,6,3],
     [77,21,32]]
ans = 0
for i in range(len(y)):
    for j in range(len(y[0])):
        ans = ans+y[j][i]
    print(ans,end = " ")
    ans = 0

