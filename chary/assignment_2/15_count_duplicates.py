#Write a program count duplicated elements in the list

def count_duplicate(x):
    y=[]
    dup={}
    count=0
    for i in x:
        i=str(i)                # required if we have string elements
        if i not in y:
            y.append(i)
        elif i not in dup:
            dup[i]=1
            count+=1
        elif i in dup:
            dup[i]= dup[i]+1
            count+=1
    return dup,count

x=[1,1,2,4,2,3,1,1,3,2,1,1,"ac","Abc","ac","ac","Abc","ac"]

total_dup_ele,dup_ele = count_duplicate(x)
print("elements wise duplicate values",total_dup_ele,"\nThe duplicate elements count is:",dup_ele)
