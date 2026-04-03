

#construct binary tree:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def getpreindex():
    return treeutils.Preindex

def incremenr():
    treeutils.Preindex+=1

def treeutils(pre,low,high):
    if low>high:
        return None
    
    root = Node(pre[getpreindex()])

    incremenr()
    if low==high:
      return root
    
    rroot = -1
    for i in range(low,high+1):                                                                                                                                    
        if pre[i]>root.data:
            rroot = i
            break

    if rroot == -1:
        rroot = getpreindex()+(high-low)
    root.left = treeutils(pre,low+1,rroot-1)
    root.right = treeutils(pre,rroot,high)


    return root

def construct(pre):
    size = len(pre)
    treeutils.Preindex=0
    return treeutils(pre,0,size-1)

def inorder(root):
    if root is None:
        return 

    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

pre = [1,2,4,5,3,6,7]
con = construct(pre)
inorder(con)


   