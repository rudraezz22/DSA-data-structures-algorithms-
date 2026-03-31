class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def level(root,k):
    if root is None:
        return 
    if k==0:
        print(root.data,end="")
    else:
        level(root.left,k-1)
        level(root.right,k-1)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left  = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    k = 2
    level(root,k)

main()

#sum of root to leaf

class node:
    def __init__(self,data):
        self.data = data
        self.left=self.right= None

def sum (r,s):
    if not r:
        return False
    if (not r.left) and (not r.right):
        return r.data==s
    return sum(r.left,s-r.data) or sum(r.right,s-r.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print(sum(root,7))
print(sum(root,10))

#k levels
class node:
    def __init__(self,data):
        self.data = data
        self.left=self.right=None

def k_levels(root,k):
    if not root or k<0:
        return -1
    
    if k==0:
        print(root.data,end="")
        return
    k_levels(root.left,k-1)
    k_levels(root.right,k-1) 

def k_nodes(root,target,k):
    if not root:
        return -1
    if root==target:
        k_levels(root,k)

        return 0
    #left
    dl = k_nodes(root.left,target,k)
    if dl!=-1:
        if dl+1 == k:
            print(root.data,end="")
        else:
          k_levels(root.right,k-dl-2)
        return dl+1
    #right
    dr = k_nodes(root.right,target,k)
    if dr!=-1:
        if dr+1== k:
            print(root.data,end="")
        else:
            k_levels(root.left,k-dr-2)
        return dr+1
    return -1


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left  = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
k_nodes(root,target,1)
