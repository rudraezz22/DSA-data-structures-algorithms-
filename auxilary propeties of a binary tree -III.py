
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def size(Node):
    if Node is None:
        return 0
    return 1+size(Node.left)+size(Node.right)

obj = None
obj = Node(20)
obj.left = Node(30)
obj.right = Node(40)
print(size(obj))
#sum of binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def sum(root):

    if root is None:
        return 0
    return sum(root.left)+sum(root.right)+root.data

obj = None
obj = Node(20)
obj.left = Node(30)
obj.right = Node(40)
obj.left.left = Node(11)
obj.left.right = Node(12)
obj.right.left = Node(13)
obj.right.right = Node(15)
print(sum(obj))


#height of the tree

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)

    return max(left,right)+1

obj1 = None
obj1 = Node(1)
obj1.left = Node(2)
obj1.right = Node(3)
obj1.left.left = Node(4)
obj1.left.right = Node(5)

print(height(obj1))

