


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
