#print1to10

def print1to10(n):
    if n>10:
        return
    print(n)

    print1to10(n+1)

print1to10(1)

#factorial

def abcd(n):
    if (n==1 or n==0): # base case
        return 1
    return n*abcd(n-1) #recursive call
input1 = int(input("enter your number"))
print(abcd(input1))
