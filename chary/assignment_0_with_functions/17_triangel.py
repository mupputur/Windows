#WAP to check whether a triangle is Equilatera, Isosceles or Scalene
def type_of_triangle(a,b,c):
    if(a==b)and(a==c):
        print("The triangle is a 'Equilateral Triangle")
    elif(a==b)or(a==c)or(b==c):
        print("The triangle is a 'Isosceles Triangle")
    else:
        print("The triangle is a 'Scalene Triangle")

for i in range(6):
    a=int(input("Enter the First angle  :"))
    b=int(input("Enter the Second angle :"))
    c=int(input("Enter the Thired angle :"))
    if(a+b+c)==180:
        type_of_triangle(a,b,c)
    else:
        print("The triangle is not possible with the given values")
