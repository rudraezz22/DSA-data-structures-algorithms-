
#armstrong number

number = int(input("enter ur number"))
digit = len(str(number))
result = 0

temp = number

while temp>0:
    remain = temp%10 
    result += remain**digit
    temp = int(temp/10) #or //10

if result == number:
    print("this is an armstrong number")
else:
    print("its not an armstrong number")


#factors:

n = int(input("enter ur number"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)

#roman numbers

n = input("enter roman number")
dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}

result = 0

for i in range(0,len(n)-1):
   if dict[n[i]]<dict[n[i+1]]:
       result-= dict[n[i]]
   else:
       result+=dict[n[i]]

print(f"{result+dict[n[-1]]}")

