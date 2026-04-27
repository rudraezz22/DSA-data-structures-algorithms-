# b tree implementation
class BTree:
    def __init__(self,Tree,leaf=False):
        self.leaf = leaf
        self.Tree = Tree
        self.children = []
        self.keys = []


    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[len(self.keys)].traverse()

    def search(self,k):
        i = 0
        while i<len(self.keys) and k>self.keys[i]:
            i+=1

        if i<len(self.keys) and k==self.keys[i]:
            return self
        if self.leaf:
            return None
        
        return self.children[i].search(k)
    
class BTREE1:
    def __init__(self,t):
        self.root = None
        self.t =t

    def traverse(self):
        if self.root is None:
           pass
        else:
            self.root.traverse()

    def search(self,k):
        if self.root is None:
            return None
        else:
            return self.root.search(k)


obj = BTREE1(3)
obj.root = BTree([3,False])
obj.root.keys = [5,20]
obj.root.children = [BTree(3,True),BTree(3,True),BTree(3,True)]
obj.root.children[0].keys = [2,3]
obj.root.children[1].keys = [4,5]
obj.root.children[2].keys = [6,7]

r = obj.search(5)
if r:
    print("found")
else:
    print("not found")