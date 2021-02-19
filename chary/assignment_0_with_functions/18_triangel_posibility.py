#WAP to check whether a triangle can be formed by the given value for the angles
def triangle_posibility(a,b,c):
    if(a+b+c)==180:
        print("The triangle can be construct , by using the given values")
        return
    else:
        print("The triangle is not possible with the given values")
        return

for i in range(6):
    a=int(input("Enter the First angle  :"))
    b=int(input("Enter the Second angle :"))
    c=int(input("Enter the Thired angle :"))
    triangle_posibility(a,b,c)
    
    
