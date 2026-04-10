
          
######################
class ABC:
    @staticmethod
    def main(args):
        root = BST()
        root.insert(10)
        root.insert(77)
        root.insert(20)
        root.insert(50)
        root.inorder()

class Node:
    right = None
    left = None
    val = 0

    def __init__(self,val):
        self.val = val

    
class BST:
    root = None

    def insert(self,key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
        prev = None
        temp = self.root

        while temp !=None:
             if temp.val>key:
                 prev = temp
                 temp = temp.left
             elif temp.val<key:
                  prev = temp
                  temp = temp.right
        
        if prev.val >key:
           prev.left = node
        else:
            prev.right=node

    def inorder(self):
        temp=self.root
        stack=[]
        while (temp!=None or not len(stack)==0):
            if temp!=None:
                stack.append(temp)
                temp =temp.left 

            else:
                temp = stack.pop()
                print(temp.val)
                temp= temp.right

 
if __name__ == "__main__":
    ABC.main([])
                 
                 
    