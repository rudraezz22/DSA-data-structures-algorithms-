#palindrome
n = int(input("enter ur number"))

temp = n
reversed = 0

while temp >0:
    digit = temp%10
    reversed = reversed*10+digit
    temp //=10

if n == reversed :
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")

#HCF/GCD

smallest = int(input("enter ur number"))
largest = int(input("enter ur number"))

while(smallest):
    numstore = smallest
    smallest = largest%smallest
    largest = numstore

print(f"the hcf is {largest}")