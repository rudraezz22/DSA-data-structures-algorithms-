def swap(a,b):
    print(f"before swapping numbers are {a},{b}")
    a = a^b
    b = a^b
    a = a^b

    print(f"after swapping numbers are {a},{b}")


def swap2(a,b):
    print(f"before swapping numbers are {a},{b}")

    a = (a&b)+(a|b)
    b = a + (~b) +1
    a = a+(~b)+1
    print(f"after swapping numbers are {a},{b}")

swap(3,4)
swap2(2,7)


#divisionLAMA 
a = 17789
b = 5345

q = 0
remainder = a

while remainder>=b:
    remainder = remainder - b
    q = q+1

print(f"the remainder is {remainder} , quotient is  {q}")