def RabinKarp(text,pattern):
    n,m = len(text),len(pattern)
    if m>n:
        return []
    base = 256
    th=ph=0
    power = base**(m-1)

    for i in range(m):
        ph = ph*base+ord(pattern[i])
        th = th*base+ord(text[i])

    result = []
    for i in range(n-m+1):
        if ph==th and text[i:i+m]==pattern:
            result.append(i)
        if i<n-m:
            th = (th-ord(text[i])*power)*base+ord(text[i+m])
    return result
print(RabinKarp("abcdyuijeing","jeing"))

#kmp 
def KMP(text,p):
    l = [0]*len(p)
    i = 0
    for j in range(1,len(p)):
        while i>0 and p[i] !=p[j]:
            i=l[i-1]
        if p[i] == p[j]:
            i+=1
            l[j] = i
    res = []
    i=j=0
    while i<len(text):
        if text[i] == p[j]:
            i+=1
            j+=1
            if j == len(p):
                res.append(i-j)

                j = l[j-1]
        else:
            if j>0:
                j = l[j-1]
            else:
                i+=1
    return res
print(KMP("abcdyuijeing","jeing"))    
        
