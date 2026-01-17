a = "Cadingal"
dict1 = {}
def frquency(a):
    for i in range(len(a)):
        if a[i] in dict1.keys() :
            dict1[a[i]] +=1
        else:
            dict1[a[i]] = 1

    return dict1
print(frquency(a))

#anagram:
def anagram(s1,s2):
    a1 = list(s1).sort()
    a2 = list(s2).sort()

    if a1 == a2:
        print("its an anagram")

anagram("earth","heart")

#count words:
def countwords(p):
    
    count = 0

    for i in range(len(p)):
        if p[i] == " ":
            count +=1
        else:
            pass
    return count+1 #for last word
p = "i am Rudra"
print(countwords(p))




