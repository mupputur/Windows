#Write a program find a factorial of a given number

def foctorial(x):
    result=1
    for i in range(1,x+1):
        result=result*i
    return result

x=int(input("Enter the nuber to find factorial:"))

print(foctorial(x))
