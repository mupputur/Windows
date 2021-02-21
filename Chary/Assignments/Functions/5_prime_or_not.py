# Write a program find a given number is prime or not

def prime_or_not(num):
    for j in range(2,num):
        if num%j==0:
            return 1
    else:
        return 2
        
for i in range(10):
    num=int(input("Enter the number to know whether prime or not: "))
    result = prime_or_not(num)
    if num==0 or num==1 or result==1:
        print("Not a prime")
    elif result==2:
        print("Prime Number")

