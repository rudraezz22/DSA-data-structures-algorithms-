class item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight

def knapsack(w,arr):
    arr.sort(key=lambda x:(x.profit/x.weight),reverse = True)
    finalValue=0.0

    for item in arr:
        if item.weight<=w:
            w-=item.weight
            finalValue+=item.profit
        else:
            finalValue+=(item.profit*w/item.weight)
            break
    return finalValue

w=50
arr=[item(60,70),item(110,20),item(120,60)]
print(knapsack(w,arr))

    