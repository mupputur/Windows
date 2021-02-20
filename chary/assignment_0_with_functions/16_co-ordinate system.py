#WAP to accept a coordinate point in a XY coordinate system & determine in which
#coordinate point lies.
def xy_co_ordinates(x,y):
    if x==0 and y==0:
        print("The Intersection point is located at 'Origin'")
    elif x>0 and y>0:
        print("The point is lies in 1st Coordinate")
    elif x<0 and y>0:
        print("The point is lies in 2nd Coordinate")
    elif x<0 and y<0:
        print("The point is lies in 3rd Coordinate")
    elif x>0 and y<0:
        print("The point is lies in 4th Coordinate")
    else:
        print("Enter the proper value of x,y")


for i in range(7):
    x=int(input("\nEnter the value of 'X'-Coordinate:"))
    y=int(input("Enter the value of 'Y'-Coordinate:"))
    xy_co_ordinates(x,y)
    
