

#reverse

A = [10,5,13,6,78]
for i in range(1,len(A)):
    value = A[i]

    j = i - 1

    while j>=0 and value<A[j]:
        A[j+1] = A[j] 
        j -= 1
        A[j+1] = value
start = 0
end = len(A) -1


while start<end:
    A[start] , A[end] = A[end] , A[start]
    start+=1
    end-=1

print(A)