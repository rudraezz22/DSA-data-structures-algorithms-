import heapq

def jobseq(arr):

    n=len(arr)
    arr.sort(key=lambda x:x[1])
    heap=[]
    result=[]

    for i in range(n-1,-1,-1):
        if i==0:
            slots_available=arr[i][1]
        else:
            slots_available=arr[i][1]-arr[i-1][1]

        heapq.heappush(heap,(-arr[i][2],arr[i][1],arr[i][0]))

        while heap and slots_available:
          profit,deadline,jobid=heapq.heappop(heap)

          slots_available-=1

          result.append([jobid,deadline])

    result.sort(key= lambda x:x[1])
    for job in result:  
        print(job,end=" ")  
    print()
arr=[["a",4,70],["b",1,80],["c",1,30],["d",2,100],["e",3,40]]
jobseq(arr)