#Write a program find a factorial of a given number

def foctorial(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result

num=int(input("Enter the nuber to find factorial:"))
print(foctorial(num))
