
#mergeTWOSORTEDARRAY
x = [1,4,7,9,22]
y = [2,6,8,12]

combined = x+y
def abcd(combined):
  if len(combined)>1:
    mid = len(combined)//2
    left = combined[:mid]
    right = combined[mid:]
    abcd(left)
    abcd(right)


    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            combined[k] = left[i]
            i+=1
        else:
            combined[k] = right[j]
            j+=1
        k+=1
    
    while i<len(left):
        combined[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        combined[k] = right[j]
        j+=1
        k+=1
print(f"unsorted aray :{combined}")
abcd(combined)
print(f"sorted array: {combined}")

