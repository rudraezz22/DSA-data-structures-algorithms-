

#implementation of pririty queue using list

class pq:
    def __init__(self):
        self.q=[]
    
    def nque(self,value,priority):
        self.q.append((value,priority))

    def isempty(self):
        return len(self.q)==0
    
    def peek(self):
        if self.q:
            self.q.sort(key=lambda x:x[1],reverse = True)
        else:
            return None
        
        return self.q[0][0]
    
    def deque(self):
        if self.isempty():
            return None
        else:
            self.q.sort(key=lambda x : x[1] , reverse = True)
            return self.q.pop(0)[0]
        
b = pq()
b.nque("low",1)
b.nque("mid",2)
b.nque("high",3)
b.nque("urgent",4)
print(b.peek())
print(b.deque())
print(b.peek())
print(b.isempty())
    