#Write a program that should convert lower case to upper case letter?
def lower_to_upper(ip_str):
    new_str=""
    for ch in ip_str:
        if ord(ch)>=97 and ord(ch)<=122:
            ch=chr(ord(ch)-32)
        new_str=new_str+ch
    return new_str

ip_str=input("Enter the string to convert uppercase letters: ")
print(lower_to_upper(ip_str))
