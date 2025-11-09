

def paren(s,l,r,p,n):
    if p == 2*n:
        for ss in s:
            print(ss , end='')
        print("\n")
        return
    if l>r:
        s[p] = "}"
        paren(s,l,r+1,p+1,n)
    if l<n:
        s[p] = "{"
        paren(s,l+1,r,p+1,n)
    

n = int(input("enter the number of parenthesis"))
l = 0
r = 0
p = 0
s = [""]*2*n
paren(s,l,r,p,n)

    