def reversenumber(num):
    last = num%10
    if num>0:
        last = num%10
        if num//10>0:
            current = reversenumber((int)(num//10))
            return last*pow(10,len(str(current))) + current
        return num
num = 56883
print(f"{reversenumber(num)}")
        

def reverseString(s):
    if len(s) == 1:
        return s[0]
    firstchar = s[0]
    return reverseString(s[1:]) + firstchar
s = "rudra"
print(reverseString(s))


#power of 4

n = int(input("enter the number"))

def powercheck(n):
    if n <=0:
      return False
    if n==1:
        return True
    if (n%4) == 0:
        return powercheck(n/4)
    return False
print(powercheck(n))