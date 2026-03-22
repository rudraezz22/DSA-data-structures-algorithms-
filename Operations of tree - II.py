from collections import deque



#searching

class Node:
   def __init__(self,data):
      self.data = data
      self.left = None
      self.right =None

def insert(root,data):
   nnode = Node(data)
   if root is None:
      return nnode
   q = deque()
   q.append(root)
   while q:
      temp = q.popleft()
      if temp.left is None:
         temp.left = nnode
         break
      else:
         q.append(temp.left)
      if temp.right is None:
         temp.right = nnode
         break
      else:
         q.append(temp.right)
   return root

def search(root,key):
   if root is None:
      return None
   q = deque([root])
   while q:
      temp = q.popleft()
      if temp.data == key:
         return True
      if temp.left:
         q.append(temp.left)
      if temp.right:
         q.append(temp.right)
   return False



obj = None
obj = insert(obj,5)
obj = insert(obj,6)
obj = insert(obj,7)
obj = insert(obj,8)
obj = insert(obj,9)


key = 61

if search(obj,key):
   print("True")
else:
   print("False")