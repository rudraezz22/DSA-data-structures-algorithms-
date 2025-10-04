def abcd(set,setsize):
    powersetsize = 2**setsize
    inner = 0
    outer = 0

    for outer in range(0,powersetsize):
      for inner in range(0,setsize):
         if (outer &(1<<inner) >0):
            print(set[inner],end=" ")
      print("")
    
size = int(input("enter size of set"))
set = []
for i in range(0,size):
       n = int(input("enter the element"))
       set.append(n)

abcd(set,size)

#flip

def flip1(num1,num2):
    flip = 0
    while (num1>0 or num2>0 ):
        t1 = num1&1
        t2 = num2&1

        if t1 != t2:
            flip += 1
        
        num1>>=1
        num2>>=1
    return flip


num1 = int(input("enter your input 1:"))
num2 = int(input("enter 2nd input"))

print(flip1(num1,num2))
