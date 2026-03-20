class Node:
    def __init__(self,v):
        self.v , self.l , self.r = v,None,None

root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)
root.r.l = Node(6)
root.r.r = Node(7)

def inorder(node):
    if node:
        inorder(node.l)
        print(node.v,end="")
        inorder(node.r)

def preorder(node):
    if node:
        print(node.v,end="")
        preorder(node.l)
        preorder(node.r)

def postorder(node):
    if node:
        postorder(node.l)
        postorder(node.r)
        print(node.v,end="")


inorder(root)
print("\n")
preorder(root)
print("\n")
postorder(root)
print("\n")