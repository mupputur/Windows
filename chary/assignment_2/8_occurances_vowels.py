#Write a program count number of occurrences of vowels in a given string

def occurrences_of_vowels(y):
    vowels="AEIOU"
    count_vowels={}
    
    for j in y:
        if j in vowels and j not in count_vowels :
            count_vowels[j]=1
        elif j in vowels and j in count_vowels :    
            count_vowels[j]=count_vowels[j]+1
    return count_vowels        


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

x=input("Enter the string: ")
y=vowels_uppercase(x)
print(occurrences_of_vowels(y))



