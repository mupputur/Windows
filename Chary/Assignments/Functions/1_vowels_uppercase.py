#Write a program convert all the vowels to uppercase for the given input
#string.

def vowels_uppercase(given_str):
    new_str=""
    vowels="aeiou"
    for ch in given_str:
        if ch in vowels:
            new_str=new_str+chr(ord(ch)-32)
        else:
            new_str=new_str + ch
    return new_str


given_str=input("Enter the text message:")

print(vowels_uppercase(given_str))
    
