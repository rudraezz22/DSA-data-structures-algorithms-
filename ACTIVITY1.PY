def headrec(n,num):
    if n>num:
        return
    headrec(n+1,num)
    print(n)
n = int(input("enter the number"))
headrec(1,n)

#tail recursion

def tailrec(n,num):
    if n > num:
        return
    print(n)
    tailrec(n+1,num)
n = int(input("enter the number"))
tailrec(1,n)

#tree recursion

def tree(n,num):
    if (n<1 or n>num):
        return
    print(n)

    tree(n-1,num)
    print(n)

n = int(input("enter ur number"))

tree(n,n)
