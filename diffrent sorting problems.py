def rotations(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)
def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size-1):
       
        a[i] = a[i+1] 
    a[a_size-1] = temp

def print1(a,a_size):
    print(a, end=" ")

a = [2,5,71,22,3]
print1(a,len(a))
rotations(a,2,len(a))
print1(a,len(a))


#check array sorted and rotated
a = [3,4,5,2,1]
n = len(a)
count = 0

for i in range(1,n):
    if a[i-1]>a[i]:
        count+=1

if a[0]<a[n-1]:
    count+=1

print(count<=1)