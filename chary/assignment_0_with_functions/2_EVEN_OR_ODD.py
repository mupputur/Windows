#WAP TO CHECK WHETHER A GIVEN NUMBER IS EVEN OR ODD BY USING FUNCTIONS
def Even_or_Odd(x):
    if x%2 is 0:
        return True
    else:
        return False

x=int(input("Enter the Number"))
if Even_or_Odd(x):
    print("The given number is a Even number")
else:
    print("The given number is a Odd number")
