def ascii(string1):
    l1 = []

    for i in string1:
        n = ord(i)
        if n//10:
            maxi = 0
            while n>0:
                if n%10>maxi:
                    maxi=n%10
                n//=10
            l1.append(maxi)
        else:
            l1.append(n)
    return sum(l1)

print(ascii("rudra"))

#lexicograaphically next

def lexicoNext(s2):
    if s2 == "":
       return "a"
    
    i = len(s2)-1
    while s2[i] == "z" and i>=0:
        i-=1
    if i==-1:
        s2 = s2+"a"
    else:
        s2 = s2.replace(s2[i],chr(ord(s2[i])+1),1)
    return s2
print(lexicoNext("pdtx"))