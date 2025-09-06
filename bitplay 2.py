
#2oddnumber

def oddTWO(arr,size):
  result = arr[0]
  x=0
  y=0
  set_bit=0

  for i in range(1,size):
      result = result ^arr[i]
  set_bit = result& ~(result-1)

  for i in range(size):
      if (arr[i]&set_bit):
          x=x^arr[i]
      else:
          y = y^arr[i]

  print(f"these are odd occuring no.{y}{x}")

arr = []
size = int(input("enter the size of array"))
for i in range(size):
    element = int(input("enter ur element"))
    arr.append(element)

oddTWO(arr,size)


