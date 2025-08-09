#1st method

def func1(n):
    sum = 0

    return n*(n+1)/2

print(func1(4))

#no. of iteration is 1 : because the calculation is happening 1 time

#2nd method
def func2(n):
  sum = 0
  for i in range(1,n+1):
     sum+=i
  return sum

print(func2(4))

#no. of iterations will be same as n: bacause the loop is iterating n number of times

#method 3

def func3(n):
   sum = 0 

   for i in range(1,n+1):
      for j in range(1,i+1):
         sum+=1
   return sum

print(func3(4))

#the no. of iterations will be the final sum : because the loop is iterating the same no. of times as the final sum as out and inner loop are there


#fibonacchi series

n = 10
a = 0
b =1
print(a,end=" ")
print(b,end=" ")
for i in range(n):
   c = a+b
   print(c,end=" ")
   a=b
   b=c

#factorial

n=4
fact = 1
for i in range(1,n+1):
   fact=fact*i

print("\n",fact)
