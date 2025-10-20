def check(a):
    length = len(a)

    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and check(a[1:])

a = [1,2,3,4,5,12,56]

if check(a):
    print("list is sorted")
else:
    print("list is not sorted")
        

def totalsum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + totalsum(a[1:])

a = [5,9]

print(f"the total sum is {totalsum(a)}")


#max 

def maxx(a):
    length = len(a)
    if length == 1:
      return a[0]
    return max(a[0],maxx(a[1:]))

a = [1,2,3,4,5,12,56]
print(f"the max number is{maxx(a)}")