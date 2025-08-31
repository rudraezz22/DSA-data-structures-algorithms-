
#checking number of bits
def numofbits(n):
    ones=0
    zeroes=0

    while n :
        if(n&1==n):
            ones+=1
        else:
            zeroes+=1
        
        n>>=1
    print(f"no. of ones{ones},no. of zeroes{zeroes}")

numofbits(int(input("enter the number")))

#SetorNOT:

def setornot(number,n):
    if number&(1<<(n-1)):
        print("Its a SET")
    else:
        print("Its a NOT")

setornot(int(input("enter ur number")),int(input("enter the bit")))