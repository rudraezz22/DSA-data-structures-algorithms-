a = ''' c o d i
 ngal'''
result = ''''''
for i in a:
    if i !=" " and i != "\n" and i!="\t":
        result+=i
    else:
        pass
print(result)