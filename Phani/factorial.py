#Write a program find a factorial of a given number

def factorial(num):
    fact=num
    for i in range(1,num):
        fact=fact*(num-i)
    return fact
print(factorial(int(input("enter the number:"))))
