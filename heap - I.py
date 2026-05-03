class Heap:
    arr = []
    heapsize = 0
    maxheapsize = 0
    
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.arr = [None]*maxsize
        self.heapsize = 0

    def maxheapify(self,i):
        l = self.lchild(i)
        r = self.rchild(i)
        largest = i

        if l<self.heapsize and self.arr[l]>self.arr[i]:
            largest = l
        if r<self.heapsize and self.arr[r]>self.arr[largest]:
            largest = r

        if i !=largest:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp

            self.maxheapify(largest)

    def parent(self,i):
        return (i-1)//2
    def lchild(self,i):
        return (2*i+1)
    def rchild(self,i):
        return (2*i+2)
    
    def removemax(self):
        if self.heapsize<=0:
            return None
        if self.heapsize==1:
            self.heapsize-=1
            return self.arr[0]
        
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapsize-1]
        self.heapsize-=1
        self.maxheapify(0)
        return root
    def increasekey(self,i,newval):
        self.arr[i] = newval
        while i!=0 and self.arr[self.parent(i)]<self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i =self.parent(i)
    def getmax(self):
        return self.arr[0]
    def cursize(self):

        return self.heapsize
    
    def delete(self,i):
        self.increasekey(i,float("inf"))
        self.removemax()

    def insert(self,x):
        if self.heapsize==self.maxsize:
            print("overflow cannot be insertes")
            return 
        
        self.heapsize+=1
        i = self.heapsize-1
        self.arr[i] = x


        while i != 0 and self.arr[self.parent(i)]<self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)]  = temp
            i = self.parent(i)

obj = Heap(15)

k,i,n = 6,0,6
obj.insert(4)
obj.insert(5)
obj.insert(12)
obj.insert(22)
obj.insert(1)

print("the current size is:",obj.cursize())
print("the max element is :" , obj.getmax())
obj.delete(3)
print("the current size is:",obj.cursize())
obj.insert(34)
obj.insert(31)
print("the current size is:",obj.cursize())

print("the max element is :" , obj.getmax())