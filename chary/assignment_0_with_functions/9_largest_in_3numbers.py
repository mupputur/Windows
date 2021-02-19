# WAP TO FIND THE LARGEST OF THREE NUMBERS BY USING FUNCTIONS
def largest_number(x,y,z):
    if((x>y) and (x>z))or(x>y and y==z ):
        print("X is the Largest Number")
    elif(x<y)and (y>z) or (x==z and y>z):
        print("Y is the Largest Number")
    elif((x<z)and (y<z))or(x==y and x<z):
        print("Z is the Largest Number")
    elif(x==y and y==z):
        print("The given 3 numbers are equal,The maximum values is",x)
    elif(x==y)and(x>z):
        print("The X & Y both the numbers are Larger,\nThe Largest value is:",x)
    elif(y==z)and(y>x):
        print("The Y & Z both the numbers are Larger,\nThe Largest value is:",y)
    elif(x==z)and(x>y):
        print("The X & Z both the numbers are Larger,\nThe Largest value is:",z)




x=int(input("Enter the First number X :"))
y=int(input("Enter the second number Y :"))
z=int(input("Enter the second number Z :"))

largest_number(x,y,z)
    
