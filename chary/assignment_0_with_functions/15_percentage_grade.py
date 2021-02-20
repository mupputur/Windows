#WAP to read roll no, name and marks of three subjects and calculate the
#total , percentage and division.
def percentage_division(m,p,c,total):
    if m<=100 and p<=100 and c<=100 and total<=300:
        print("Tatal marks is :",total)
        p=(total/3)
        print("The obtained marks in percentage is:",p)
    if p>=60:
        print( "Result Status is:'First class'")
    elif p<60 and p>=48:
        print("Result Status is:'Second Class'")
    elif p<48 and p>=36:
        print(" Result Status is:Pass")
    elif p<36:
        print("Result Status is:Failed")
    
for i in range(5):
    roll=input("\nEnter the roll number:")
    name=input("Enter the Name:")
    print("Enter the Marks details\n")
    m=int(input("Enter the Marks in Mathematics :"))
    p=int(input("Enter the Marks in Physics     :"))
    c=int(input("Enter the Marks in Cemistry    :"))
    print("The Given Roll Number is:",roll)
    print("The Given Name is:",name)
    total=m+p+c
    if m<=100 and p<=100 and c<=100:
        percentage_division(m,p,c,total)
    else:
        print("Each subject value should be lessthan or equal to 100")
