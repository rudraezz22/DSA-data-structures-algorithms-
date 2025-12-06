def zeroandOne(A,n): #no sorting algo used
    count = 0
    for i in range(0,n):
        if (A[i] == 0):
            count = count+1

    for i in range(0,count):
        A[i] = 0
    for i in range(count,n):
        A[i] = 1
    
A = [0,1,0,0,0,1,1,0,0,1,1,0,1,0,1]
print(f"unsorted array: {A}")
zeroandOne(A,len(A))
print(f"Sorted array: {A}")

#UNION OF ARRAY
def unionOFarrys(A,B,n,m):
    i,j=0,0

    while i<n and j<m:
        if A[i]<B[j]:
            print(A[i], end=" ")
            i+=1
        elif B[j]<A[i]:
            print(B[j], end=" ")
            j+=1
        else:
            print(A[i],end=" ")
            i+=1
            j+=1

    
A=[2,4,16,77,103]
B=[1,44,91,304,1001]
n = len(A)
m = len(B)
unionOFarrys(A,B,n,m)