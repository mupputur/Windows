# Command line argumnets
#WAP which is a menu- Driven program to compute
#the area of the various geometrical shape.
import sys
def circle(r):
    print("Area of circle is:",3.14*r*r,end="cm^2\n")
def rectange_area(l,b):
    print("Area of the 'Rectangle' is:",l*b,end="cm^2\n")
def Triangle_area(b,h):
    print("Area of the 'Triangle' is:",0.5*b*h,end="cm^2\n")

argv=sys.argv[1:]
words=["HELP","Help","help"]
if len(argv)==0:
    print("in valid input, use 'Help' key to know more details")
    sys.exit(0)
if argv[0] in words:
    print("select 'C' for Circle Area")
    print("select 'R' for Rectangle Area")
    print("select 'T' for Triangle Area")
    ip=input()
else:
    ip=argv[0]
if len(ip)==0 or (ip not in "CRT"):
    print("please provide the valid input, Thanking you\n")
    sys.exit(0)
if ip=="C"or ip=="c" :
    r=int(input("enter Radius: "))
    circle(r)
if ip=="R" or ip=="r":
    l=int(input("Enter length: "))
    b=int(input("Enter bredth: "))
    rectange_area(l,b)
if ip=="T" or ip=="t":
    b=int(input("Enter bredth: ")) 
    h=int(input("Enter height: "))
    Triangle_area(b,h)
    
