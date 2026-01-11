

#no vowels
def CheckVowels(s1):
    vowels = "aeiou"
    result = ""
    for i in s1:
        if i in vowels:
            result+= ""
        else:
            result+=i
    return result
inp3 = input("enter to remove vowels")
print(CheckVowels(inp3))