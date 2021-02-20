#Write a program find given number is perfect or not

def is_perfect(x):
    sum1=0
    for i in range(1,x):
        if x%i==0:
            sum1=sum1+i
    if sum1==x:
        return 1
    else:
        return -1



x=int(input("Enter the number:"))
result= is_perfect(x)

if result==1:
    print("The given number is a 'Perfect' number")
elif result==-1:
    print("The given number is 'Not a perfect' number")
            
