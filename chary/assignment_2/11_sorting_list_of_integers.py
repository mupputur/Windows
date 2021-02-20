#Write a program sort the given list of integer elements

def sorting(x):
    for i in range(1,len(x)):
        for j in range(len(x)):
            if x[i]<x[j]:           # if we place > , gives desending order
                x[i],x[j]=x[j],x[i]
    return x

x=[]
for i in range(6):
    x.append(int(input("enter the elements:")))
print(x)
result=sorting(x)
print(result)
        
        
           
