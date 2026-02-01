#using linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        return True if self.head==None else False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    def top_element(self):
        if self.isempty():
            return None
        else:
            return self.head.data
        
    def pop(self):
        if self.isempty():
            return None
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node.data
        
stack1 = Stack()
stack1.push(5)
stack1.push(3)
stack1.push(3)
stack1.push(7)

print(stack1.top_element())
print("the popped elemt:" , stack1.pop())
print(stack1.top_element())
print("the popped elemt:" , stack1.pop())
print(stack1.top_element())
print("the popped elemt:" , stack1.pop())




