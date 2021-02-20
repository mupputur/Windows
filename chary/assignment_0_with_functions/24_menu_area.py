#WAP which is a menu- Driven program to compute
#the area of the various geometrical shape.
def shape_and_area(x):
    if (x is 1):
        r=int(input("Enter the 'radius' of the Circle in 'cm' :"))
        print("Area of the circle is:",3.14*r*r,end="cm^2\n")
    elif(x is 2):
        l=int(input("Enter the 'Length' of the rectangle in 'cm' :"))
        b=int(input("Enter the 'Width' of the rectangle in 'cm'  :"))
        print("Area of the 'Rectangle' is:",l*b,end="cm^2\n")
    elif(x is 3):
        b=int(input("Enter the 'Base' of the Triangle in 'cm'  :"))
        h=int(input("Enter the 'Height' of the Triangle in 'cm':"))
        print("Area of the 'Triangle' is:",0.5*b*h,end="cm^2\n")
    else:
        print("please provide the valid input, Thanking you\n")


for i in range(5):
    print("\n")
    print("Enter value '1' to Find the Area of CIRCLE     : ")
    print("Enter value '2' to Find the Area of RECTANGLE  : ")
    print("Enter value '3' to Find the Area of TRIANGLE   : ")
    x=int(input())
    shape_and_area(x)
