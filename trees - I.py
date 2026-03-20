from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(6)


print(root)

#traversing nodes

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value,end=" ")
        inorder(node.right)
def preorder(node):

    if node:
        print(node.value,end="")
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node:
      postorder(node.left)
      postorder(node.right)
      print(node.value,end="")

inorder(root)
print("\n")
preorder(root)
print("\n")
postorder(root)
print("\n")