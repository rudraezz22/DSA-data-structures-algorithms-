class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

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
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


r = Node(10)
r = insert(r,20)
r = insert(r,11)
r = insert(r,33)
r = insert(r,5)
inorder(r)

def search(root,data):
    if root is None or root.data == data:
        return root
    else:
        if root.data<data:
            return search(root.right,data)
        return search(root.left,data)
    
r1 = Node(50)
r1.left = Node(30)
r1.right = Node(60)
r1.left.left = Node(20)
r1.left.right =Node(35)
r1.right.left = Node(55)
r1.right.right = Node(100)
print("\n")
inorder(r1)

key = 33
result = search(r1,key)
if result:
    print("result found: ",result.data)
else:
    print("key not found")