# WAP to check whether an alphabet is a vowel or consonant
def vowel_or_not(ch):
    #vowels=('a','e','i','o','u','A','E','I','O','U')
    vowels="aeiouAEIOU"
    if ch in vowels:
        return "The given alphabet is: 'Vowel'"
    else:
        return "The given alphabet is: 'Consonant'"


ch=input("Enter a alphabet :")

output = vowel_or_not(ch)
print(output)
