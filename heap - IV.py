
import heapq

def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

def heapify(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[largest]<arr[l]:
        largest = l
    if r<n and arr[largest]<arr[r]:
        largest = r

    if i !=largest:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

arr = [9,3,21,1,12]
heapsort(arr)
n = len(arr)
for i in range(n):
    print(arr[i] , end=" ")

#implementation direct

def descendingorder(arr):
    minheap = []
    for i in arr:
        heapq.heappush(minheap,i)
    result = []
    while minheap:
        top = heapq.heappop(minheap)
        result.insert(0,top)

    print("\n",result,end=" ")

arr1 = [3,56,2,65,1]
descendingorder(arr1)
