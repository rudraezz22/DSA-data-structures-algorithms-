

#KEYPAD
keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printcombination(combination,output,curr,n):
    if curr == n:
        print(*output,sep=",")
        return
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        printcombination(combination,output,curr+1,n)
        output.pop()
        if (combination[curr] == 0 or combination[curr] == 1):
            return

    
combination = [3,2,4]
n = int(input("enter the length"))
printcombination(combination,[],0,n)

