#Write a program find given number is perfect or not

def is_perfect(num):
    sum1=0
    for i in range(1,num):
        if num%i==0:
            sum1=sum1+i
    if sum1==num:
        return 1
    else:
        return -1

num=int(input("Enter the number:"))
result= is_perfect(num)
if result==1:
    print("The given number is a 'Perfect' number")
elif result==-1:
    print("The given number is 'Not a perfect' number")
            
