#Write a program count number of occurrences of vowels in a given string

def occurrences_of_vowels(ip_str):
    vowels="aeiouAEIOU"
    sum_value=0
    for ch in ip_str:
        if ch in vowels:
            sum_value=sum_value+1
    return sum_value        

ip_str=input("Enter the string: ")

print("The no. of Vowels in the string is:",occurrences_of_vowels(ip_str))



