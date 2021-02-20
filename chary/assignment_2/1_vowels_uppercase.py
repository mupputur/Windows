#Write a program convert all the vowels to uppercase for the given input
#string.

def vowels_uppercase(x):
    y=[]
    vowels="aeiou"
    for i in x:
        if i in vowels:
            z=chr(ord(i)-32)
            y.append(z)
        else:
            y.append(i)
        result="".join(y)    
    return result


x=input("Enter the text message:")

print(vowels_uppercase(x))
    
