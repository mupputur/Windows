#Write a program that should convert lower case to upper case letter?
def lower_to_upper(x):
    y=""
    for i in x:
        if ord(i)>=97 and ord(i)<=122:
            y=y+chr(ord(i)-32)
        else:
            y=y+i
    return y
x=input("Enter the string to convert uppercase letters: ")

out_put=lower_to_upper(x)

print(out_put)
