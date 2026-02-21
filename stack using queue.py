from collections import deque
class Stack():
    def __init__(self):
        self.q1= deque()
        self.q2 = deque()
    def push(self,x):
        self.q2.append(x)
        while (self.q1):
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1

    def pop(self):
        if self.q1:
            self.q1.popleft()

    def top(self):
        if self.q1:
           return self.q1[0]
        else:
            return None
    

    def size(self):
        return len(self.q1)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.size())
print("the top element is",s.top())
s.pop()
print("the top element is",s.top())
s.pop()
print("the top element is",s.top())
print(s.size())
        
#using pop
class Stack1():
    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self,x):
        self.q1.append(x)
    def pop(self):
        if not self.q1:
            return 
        while len(self.q1) !=1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1


    def top(self):
        if not self.q1:
            return
        while len(self.q1) !=1:
            self.q2.append(self.q1.popleft())
        
        top = self.q1[0]
        self.q2.append(self.q1.popleft())

        self.q1,self.q2=self.q2,self.q1
        return top
    def size(self):
        return len(self.q1)

s = Stack1()
s.push(1)
s.push(2)
s.push(3)
print("-------------------")
print(s.size())
print("the top element is",s.top())
s.pop()
print("the top element is",s.top())
s.pop()
print("the top element is",s.top())
print(s.size())