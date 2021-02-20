#WAP which is a menu driven program to perform a simple calculation:
def arithmetic_operation(z):
    if z is '+':
        print("The result after Addition is:",x+y)
    elif z is "-":
        print("The result after Subtraction is :",x-y)
    elif z is "*":
        print("The result after multiplication is:",x*y)
    elif z is "/":
        print("The result after Division is:",x/y)
    elif z is "%":
        print("The remainder after modulo operation is:",x%y)
    else:
        print("Enter valid operation")

for i in range(7):
    x=int(input("Enter the First Number:"))
    y=int(input("Enter the Second Number:"))
    z=input("Enter ,Which operation you want to perform : +,-,*,/,% ")
    arithmetic_operation(z)
