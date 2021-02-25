#Write a program count duplicated elements in the list
y={}
z={}
def duplicate_count(x):
    count=0
    for i in x:
        if i not in y:
            y[i]=1
        else:
            count=count+1
            z[i]=y[i]+1

    return count
x=[10,34,20,10,34,67,20]
print(duplicate_count(x))
            
        
