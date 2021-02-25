#wap to reverse a given list
def reverse_list(x):
    for i in range(len(x)//2):
        x[i],x[len(x)-i-1]= x[len(x)-i-1], x[i]
    return x    
x=eval(input("enter the elements in list format:"))
print(reverse_list(x))
