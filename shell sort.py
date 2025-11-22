

#intersection

A = [1,2,4,7,9,11,21]
B =[2,5,7,8,11,12,13]
m = len(A)
n = len(B)
i,j=0,0

while i<m and j<n:
    if A[i] > B[j]:
        j+=1
    elif A[i] < B[j]:
        i+= 1
    else:
        print(B[j], end=" ")
        i+=1
        j+=1


