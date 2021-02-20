#WAP to check whether a character is an alphabet, digit or special character.
def type_of_alphabet(x):
    if(x>="0" and x<="9"):
        print("The given eliment is a 'Digit'")
    elif(x>="A" and x<="Z") or (x>="a" and x<="z"):
        print("The given eliment is a 'Alphabet'")
    else:
        print("The given eliment is a 'Special Character'")

for i in range(3):
    x=input("\nEnter a eliment to Know the type of character:")
    type_of_alphabet(x)
