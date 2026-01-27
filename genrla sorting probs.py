

#sort string
def sortstring(str2):
    li = []
    ans = ""
    for i in range(26):
        li.append(0)
    for i in range(len(str2)):
        ind = ord(str2[i]) - ord("a")
        li[ind]+=1
    for i in range(26):
        if li[i] >=1:
            for j in range(li[i]):
                ans+=chr(ord("a")+i)
    return ans
str2 = "afec"

print(sortstring(str2))
