#Write a program that should convert lower case to upper case letter?
def lower_to_upper(str1):
    new_str=""
    for ch in str1:
        if ord(ch)>=97 and ord(ch)<=122:
            new_str=new_str+chr(ord(ch)-32)
        else:
            new_str=new_str+ch
    return new_str
str1=input("Enter the string to convert uppercase letters: ")

out_put=lower_to_upper(str1)

print(out_put)
