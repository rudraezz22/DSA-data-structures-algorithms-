class Node:
    def __init__(self,data):
        self.data = data
        self.left=self.right=None

def inorder(root):
    if root is not None:
      inorder(root.left)
      print(root.data,end=" ")
      inorder(root.right)

def insert(root,data):
    if root is None:
        return Node(data)
    
    else:
        if root.data==data:
            return root
        elif root.data<data:
            root.right = insert(root.right,data)
        else:
            root.left = insert(root.left,data)
        return root

def minvaluenode(root):
    current = root

    while (current.left is not None):
        current = current.left

    return current

def deletion(root,data):
    if root is None:
        return root
    
    if data<root.data:
       root.left = deletion(root.left,data)
    elif data>root.data:
        root.right = deletion(root.right,data)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = minvaluenode(root.right)
        root.data = temp.data
        root.right = deletion(root.right,temp.data)

    return root



root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)

inorder(root)
print("\n")
root=deletion(root,20)
inorder(root)
print("\n")
root=deletion(root,30)
inorder(root)
print("\n")
root=deletion(root,50)
inorder(root)
print("\n")
