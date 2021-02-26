
#WAP print Fibonacci series till 100 -

def fibonacci(x):
    if x<0:
        return('Not Possible')
    elif x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return(fibonacci(x-2)+fibonacci(x-1))
for i in range(12):
    print(fibonacci(i))



     
