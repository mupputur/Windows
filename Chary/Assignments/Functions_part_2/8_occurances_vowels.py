#Write a program count number of occurrences of vowels in a given string

def occurrences_of_vowels(str2):
    vowels="AEIOU"
    count_vowels={}
    for ch2 in str2:
        if ch2 in vowels and ch2 not in count_vowels :
            count_vowels[ch2]=1
        elif ch2 in vowels and ch2 in count_vowels :    
            count_vowels[ch2]=count_vowels[ch2]+1
    return count_vowels        


def vowels_uppercase(str1):
    new_str=""
    vowels="aeiou"
    for ch1 in str1:
        if ch1 in vowels:
            new_str=new_str+chr(ord(ch1)-32)
        else:
            new_str=new_str+ch1
    return new_str

x=input("Enter the string: ")
y=vowels_uppercase(x)
print(occurrences_of_vowels(y))



