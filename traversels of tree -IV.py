from binarytree import build

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
   if root:
      inorder(root.left)
      print(root.data,end="")
      inorder(root.right)

root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

list1 = [1,2,3,4,5]
print(build(list1))
inorder(root)

#preorder 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
      print(root.data,end="")
      preorder(root.left)
      preorder(root.right)


root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

l1 = [1,2,3,4,5]
print(build(l1))
preorder(root)

#postorder:
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root:
      postorder(root.left)
      postorder(root.right)
      print(root.data,end="")

root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

l2 = [1,2,3,4,5]
print(build(l2))
postorder(root)
