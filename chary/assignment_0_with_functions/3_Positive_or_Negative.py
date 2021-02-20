#WAP TO CHECK WHETHER A GIVEN NUMBER IS POSITIVE OR NEGATIVE.

def Positive_or_Negative(x):
    if x>0:
        return 1       
    elif x<0:
        return 0
     
    
x=int(input("Enter the Integer number"))

result=Positive_or_Negative(x)

if result==1:
    print("The given number is a Positive Number")
elif result==0:
    print("The given number is a Negative Number.")
else:
    print("The given number is Neighter Positive , nor Negative, its a Natural Number")
