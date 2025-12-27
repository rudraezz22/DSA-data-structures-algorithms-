x = [[3,5],
     [56,7]]

y = [[4,1], [11,23]]
ans = [[0,0],[0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        ans [i][j] = x[i][j] + y[i][j]

for p in ans:
    print(p)

#multiplication
x = [[8,2],[4,1]]
y = [[3,8],[9,15]]
ans = [[0,0],[0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            ans [i][j] += x[i][k] * y[k][j]

for pr in ans:
    print(pr)
