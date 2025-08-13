def abcd(n):
    iterations=0
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            iterations+=1
            print("*",)
        print("")
    print(f"the value of n is{n}, the no. of itertions is {iterations}")

abcd(int(input("enter ur number")))