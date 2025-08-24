
#seive of erethoseness
def seive(num):
    l1 = [True for i in range(num+1)]
    p = 2

    while p*p<=num:
      if l1[p]==True:
          for x in range(p*p,num+1,p):
              l1[x]=False
      p +=1

    for i in range(2,num+1):
        if l1[i]:
            print(i)
       
seive(56)