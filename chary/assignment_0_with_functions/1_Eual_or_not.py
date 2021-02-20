#WAP TO ACCEPT TWO INTEGERS AND CHECK WHETHER THEY ARE EQUAL OR NOT BY USING FUNCTIONS.
def equality_chek(x,y):
    if(x==y):
        return True
    else:
        return False

x=int(input("Enter the First value: "))
y=int(input("Enter the Second value: "))

if equality_chek(x,y):
    print("Given numbers are Equal")
else:
    print("The given numbers are Not Equal")

