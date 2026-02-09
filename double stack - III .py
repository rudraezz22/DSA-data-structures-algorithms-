import math
class Node:
    def __init__(self,n):
        self.size = n
        self.ar = [None]*n
        self.top1 = math.floor(n/2)+1
        self.top2 = math.floor(n/2)
    
    def push1(self,x):
        if self.top1>0:
            self.top1 = self.top1 -1 
            self.ar[self.top1] = x
        else:
            print("stack overflow by elemetn" , x)
    
    def push2(self,x):
        if self.top2<self.size-1:
            self.top2 = self.top2+1
            self.ar[self.top2] = x
        else:
            print("stack overflow by element" , x)

    def pop1(self):
        if self.top1<=self.size/2:
            x = self.ar[self.top1]
            self.top1 = self.top1-1
            return x
        else:
            print("stack undeflow")
            exit(1)
    def pop2(self):
        if self.top2>=math.floor(self.size/2)+1:
            x = self.ar[self.top2] 
            self.top2 = self.top2-1
            return x
        else:
            print("stack underflow")
    

obj = Node(5)
obj.push1(5)
obj.push2(10)
obj.push2(10)
obj.push1(13)
obj.push2(6)
print(obj.pop1())
print(obj.pop2())

#2nd method
class NODE2:
    def __init__(self,n):
        self.size = n
        self.ar = [None]*n
        self.top1 = -1
        self.top2 = self.size

    def push1(self,x):
        if self.top1<self.top2-1:
            self.top1 = self.top1+1
            self.ar[self.top1] = x
        else:
            print("stack ovefflow")
    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2 = self.top2 - 1
            self.ar[self.top2] = x
        else:
            print("stack oveflow")
    def pop1(self):
        if self.top1>=0:
            x = self.ar[self.top1]
            self.top1 = self.top1-1
            return x
        else:
            print("stack underflow")
    def pop2(self):
        if self.top2<self.size:
            x = self.ar[self.top2]
            self.top2 = self.top2+1
            return x
        else:
            print("stack underflow")



    
obj1 = NODE2(5)
obj1.push1(5)
obj1.push2(10)
obj1.push2(10)
obj1.push1(13)
obj1.push2(6)
print(obj1.pop1())
print(obj1.pop2())
