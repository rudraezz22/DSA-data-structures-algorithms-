class Node:
    def __init__(self,data):
        self.data = data

        self.left=self.right=None

def singlechild(root):
    if root is None:
        return 
    
    if (root.left is None and root.right is not None) or (root.right is None and root.left is not None):
        print(root.data,end="")

    singlechild(root.left)
    singlechild(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
singlechild(root)

#tilt of tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left=self.right=None

def traverse(root,tilt):
    if not root:
        return 0
    left = traverse(root.left,tilt)
    right = traverse(root.right,tilt)
    tilt[0]+=abs(left-right)

    return left+right+root.data

def tilt(root):
    tilt = [0]
    traverse(root,tilt)
    return tilt[0]

root = Node(4)
root.left = Node(2)
root.right = Node(9)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.right = Node(7)

print("\n",tilt(root))

#largest subtree of bst

class Node:
    def __init__(self,data):
        self.data = data
        self.left=self.right=None

class Info:
    def __init__(self,size,minval,maxval,isbst):
        self.size = size
        self.min = minval
        self.max = maxval
        self.isbst = isbst

def largest(root):
    if root is None:
        return Info(0,float("inf"),float("-inf"),True)
    
    if root.left is None and root.right is None:
        return Info(1,root.data,root.data,True)
    
    left = largest(root.left)
    right = largest(root.right)

    c = 1+left.size+right.size

    if left.isbst and right.isbst and left.max<root.data<right.min:
        return Info(c,min(left.min,root.data),max(right.max,root.data),True)
    return Info(max(left.size,right.size),float("inf"),float("-inf"),False)
50,30,60,5,20,45,70,80
root = Node(50)
root.left = Node(30)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(45)
root.right.right = Node(70)
root.right.right.right = Node(80)
result = largest(root)
print(result.size)