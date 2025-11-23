def partition(arr,low,high):
    pivot = arr[high]
    i = low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            (arr[i],arr[j]) = (arr[j] , arr[i])
    (arr[i+1] , arr[high]) = (arr[high] , arr[i+1])
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1) #high to left
        quickSort(arr,pi+1,high) #low to right
arr = [3,6,4,73,8,5,32,9]
print(f"array before sorting{arr}")
n = len(arr) -1

quickSort(arr,0,n)
print(f"after sorting{arr}")