ar = [0 for _ in range(10)]
n = 10

rear = -1
front = -1

def enqueue(item):
    global n
    global front
    global rear
    
    if rear == n-1:
        print("queue overflow")
        print("\n")
        return
    else:
      if front == -1 and rear== -1:
        front = 0
        rear = 0
      else:
        rear+=1
      ar[rear] = item

      print("item inserted")
      print("\n")

def dequeue():
   global n
   global front
   global rear

   if front == -1 or front>rear:
      print("queue underflow")
      print("\n")
      return
   else:
      item = ar[front]
      print(f"element to be delted is {item}")
      print("\n")
      if rear == front:
         rear= -1
         front= -1
      else:
         front+=1

def display():
   global n
   global front
   global rear

   if front == -1:
      print("queue is empty")
      print("\n")
      return
   else:
      i = front
      while i<=rear:
         print(ar[i],end=" ")
         
         i+=1
      print("\n")
def fronte():
   global n
   global front
   global rear

   if front == -1:
      print("queue underflow",end="")
      print("\n")
      return
   else:
      print(ar[front],end="")
      print("\n")

ch = None
print("1.for enqueue")

print("2. for dequeue")

print("3. for display front ")

print("4. for display all ")

print("5. foe exit")
condition = True
while condition:
   ch = int(input("entter input from 1-5"))
   print("\n")
   if ch==1:
      p = int(input("enter element to enqueue"))
      print("\n")
      enqueue(p)
   elif ch==2:
      dequeue()
   elif ch ==3:
      fronte()
   elif ch==4:
      display()
   elif ch==5:
      exit()

   condition!=5

