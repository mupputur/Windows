
#WAP find a factorial of a given number-

def factorial(x):
    z=x
    for i in range(1,x):
        z=z*(x-i)
    return z
        

print(factorial(int(input('enter a value:'))))
