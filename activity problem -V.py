def activity(s,f):
    n=len(f)
    i=0
    print(i,end=" ")
    for j in range(1,n):
        if s[j]>=f[i]:
            print(j,end=" ")
            i=j
s=[1,3,0,5,8,5]
f=[2,4,6,7,9,9]
activity(s,f)


#using array:
def Activity1(arr,n):
    selected=[]
    arr.sort(key=lambda x:x[1])

    i=0
    selected.append(arr[i])
    for j in range(1,n):
        if arr[j][0]>=arr[i][1]:
            selected.append(arr[j])
            i=j
    return selected


activity2=[[5,9],[1,2],[3,4],[0,6],[5,7],[8,9]]
n=len(activity2)

selected=Activity1(activity2,n)
print(selected[0],end="")
for i in range(1,len(selected)):
    print(",",end=" ")
    print(selected[i],end=" ")
