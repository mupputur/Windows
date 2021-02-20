# Write a program find a given number is prime or not

def prime_or_not(x):
    if x==0:
        return 1
    elif x==1:
        return -1
    for j in range(2,x):
        if x%j==0:
            return 2
    else:
        print("Prime Number")
        

x=int(input("Enter the number to know whether prime or not: "))
result = prime_or_not(x)
if result==1:
    print("The Zero is neither prime nor composite")
elif result==-1:
    print("Non Prime under special categoery")
elif result==2:
    print("Not a prime")

