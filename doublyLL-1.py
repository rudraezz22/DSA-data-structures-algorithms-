class Node:
    def __init__(self,data):
        self.data= data
        self.prev = None
        self.next = None

class  DoublyLL:
    def __init__(self):
        self.head = None
    def insert_beg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = ne
        ne.prev = temp

    def display(self):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end = " ")
                temp=temp.next

l = DoublyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n1.prev = n
l.display()
print("\n")
l.insert_beg(100)
print("\n")
l.display()
print("\n")
l.insert_end(100)
l.display()

        
#deletion
class node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev = None
class dobulyLL:
    def __init__(self):
        self.head = None
    def del_beg(self):
        if self.head !=None:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp = None
    def del_end(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None
    
    def display(self):
        if self.head ==None:
            print("empty list")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end = " ")
                temp = temp.next

l1 = dobulyLL()

n = node(10)
l1.head = n
n1 = node(20)
n.next = n1
n2 = node(30)
n1.next = n2
n2.prev = n1
print("\n")
l1.display()
print("\n")
l1.del_beg()
l1.display()
print("\n")
l1.del_end()
l1.display()


