from sys import maxsize
def create():
    stack = []
    return stack
def isempty1(stack):
    return len(stack) == 0
def add(stack,element):
    stack.append(element)
    print(element," is pushed into stack")
def pop(stack):
    if isempty1(stack):
        return str(-maxsize -1)
    return stack.pop()
def peek(stack):
    if isempty1(stack):
        return str(-maxsize -1)
    return stack[len(stack)-1]

stack = create()
add(stack,10)
add(stack,20)
add(stack,30)
print(stack.pop())


#stockspan
def stockspan(price , s):
    n = len(price)
    st = []
    st.append(0)
    s[0] = 1
    for i in range(1,n):
       while len(st)>0 and price[st[-1]]<=price[i]:
           st.pop()
       s[i] = i+1 if len(st) == 0 else i-st[-1]
       st.append(i)


def print1(s,n):
    for i in range(0,n):
        print(s[i],end=" ")

price = [10,4,5,90,120,80]
s = [0  for i in range(len(price)+1)]
stockspan(price,s)
print1(s,len(price))


      

