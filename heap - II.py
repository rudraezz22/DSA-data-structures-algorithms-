class Heap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    def parent(self,i):
        return (i-1)//2
    def childleft(self,i):
        return (2*i+1)
    def childright(self,i):
        return (2*i+2)
    def get(self,i):
        return self.items[i]
    def getmax(self):
        if self.size() == 0:
            return None
        return self.items[0]
    
    def extractmax(self):
        if self.size()==0:
            return None
        largest = self.getmax()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.maxheapify(0)
        return largest
    
    def maxheapify(self,i):
        l = self.childleft(i)
        r = self.childright(i)

        if (l<=self.size()-1 and self.get(l) >self.get(i)):
            largest = l
        else:
            largest = i

        if (r<=self.size()-1 and self.get(r)>self.get(largest)):
            largest = r
        if largest!=i:
            self.swap(largest,i)
            self.maxheapify(largest)

    def swap(self,i,j):
        self.items[i],self.items[j] = self.items[j] , self.items[i]

    def insert(self,key):
        index = self.size()
        self.items.append(key)
        while index!=0:
            p = self.parent(index)
            if self.get(p)<self.get(index):
                self.swap(p,index)
            index = p

obj = Heap()
print("menu: insert data , max get,max extract , quit" )

while True:
    do = input("please enter ur operations").split()
    operation = do[0].strip().lower()
    if operation == "insert":
        data = int(do[1])
        obj.insert(data)

    elif operation =="max":
        suboperation =do[1].strip().lower()
        if suboperation == "get":
            print(obj.getmax())
        elif suboperation == "extract":
            print(obj.extractmax())

    elif operation == "quit":
        break

        