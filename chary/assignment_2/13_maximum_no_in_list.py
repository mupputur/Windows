#Write a program find a maximum number in the given input integer list.

def maximum_no(x):
    maxi=x[0]
    for i in range(len(x)):
        if x[i]>maxi:
            maxi=x[i]
    return maxi

x=[]
for i in range(6):
    x.append(int(input("enter the elements:")))
print(x)
result=maximum_no(x)

print(result)





            
