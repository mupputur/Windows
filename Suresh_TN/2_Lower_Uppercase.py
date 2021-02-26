
#WAP to convert lower case to upper case letter -


def lower_upper(y):
    z=[]
    for i in y:
        q=chr(ord(i)-32)
        z.append(q)
    return z
    

    
print(lower_upper(input('enter the string:')))
