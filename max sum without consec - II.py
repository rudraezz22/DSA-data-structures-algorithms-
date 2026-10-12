def maxsum(l1):
    n = len(l1)

    if n==0:
        return 0
    if n==1:
        return max(0,l1[0])

    include = max(0,l1[0])
    exclude=0

    for i in range(1,n):
        new_include = l1[i]+exclude
        new_exclude = max(include,exclude)

        include,exclude=new_include , new_exclude
    return max(include,exclude)

l1=[2,3,7,10]
print(maxsum(l1))