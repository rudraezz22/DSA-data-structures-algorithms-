class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    
    def swap(self,n1,n2):
        PrevNode1 = None
        PrevNode2 = None
        node1 = self.head
        node2 = self.head
        if self.head == None:
            return
        
        while node1 != None and node1.data != n1:
            PrevNode1 = node1
            node1 = node1.next 
        while node2 !=None and node2.data != n2:
            PrevNode2 = node2
            node2 = node2.next

        if node1 != None and node2 != None:
            if PrevNode1 != None:
                PrevNode1.next = node2
            else:
                self.head = node2
        
            if PrevNode2 != None:
                PrevNode2.next = node1
            else:
                self.head = node1
        
            temp = node1.next
            node1.next = node2.next
            node2.next = temp

        else:
            print("swapping is not possible")

    def display(self):
        if self.head == None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
               print(temp.data,"-->",end=" ")
               temp = temp.next

l = LL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
l.display()
print("\n")
l.swap(20,40)
l.display()


