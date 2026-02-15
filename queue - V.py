class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front=self.rear=None

    def empty(self):
        return self.front==None
    def enqueue(self,item):
        temp = Node(item)
        if self.rear==None:
            self.front=self.rear = temp
            return
        
        
        self.rear.next = temp
        self.rear = temp
    def dequeue(self):
        if self.empty():
          return
        temp = self.front
        self.front = temp.next

        if (self.front==None):
            self.rear = None

obj = Queue()
obj.enqueue(20)
obj.enqueue(33)
obj.enqueue(24)
obj.dequeue()
obj.enqueue(19)
print(obj.front.data)
print(obj.rear.data)


#queue by doublyLL
class Node1():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubllyQue():
    def __init__(self):
        self.front=self.rear = None
    def isempty(self):
        return self.front == None
    def i_front(self,item):
        nnode=Node(item)
        if self.isempty():
            self.rear = self.front = nnode
        nnode.next=self.front
        self.front.prev=nnode
        self.front=nnode
        print("item inserted in front!/n")
    def i_rear(self,item):
        newnode=Node(item)
        if self.isempty():
            self.front=self.rear=newnode
        
        newnode.prev = self.rear
        self.rear.next = newnode
        self.rear = newnode
        print("item inserted at rear!")

    def delete_front(self):
        if self.isempty():
            print("queue is empty")
            return 
        if self.rear == self.front:
          self.front==self.rear==None
        else:

          self.front = self.front.next
          self.front.prev = None
    def delete_rear(self):
        if self.isempty():
            print("empty queue")
            return
        if self.rear == None:
            self.front=self.rear=None
        else:
            self.front = self.front.prev
            self.front.next = None
            print("deleted succesfully")

    def display(self):
        if self.isempty():
            print("empty queue")
            return
        temp = self.front
        print("the elements are")
        while temp:
           
            print(temp.data,end=" ")
            temp=temp.next

obj1 = DoubllyQue()
while True:
  print("enter ur choice 1.insert front 2. insert rear 3.delete front 4. delte rear 5. display")
  inp1 = int(input("enter u choice"))
  if inp1 ==1:
      input2 = int(input("enter value to be inserted"))
      obj1.i_front(input2)
  elif inp1 ==2:
      input2 = int(input("enter value to be inserted"))
      obj1.i_rear(input2)
  elif inp1 ==3:
      
      obj1.delete_front()
  elif inp1 ==4:
      obj1.delete_rear()
  elif inp1==5:
      obj1.display()
  else:
      print("enter a valid choice")
      break



    