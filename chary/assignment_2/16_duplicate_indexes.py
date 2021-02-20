#Write a program to get the indices of duplicated elements from given
#input list.
def count_duplicate(x):
    y=[]
    z=[]
    dup={}
    count=0
    for i in range(len(x)):
        x[i]=str(x[i])
        if x[i] not in y:
            y.append(x[i])
        elif x[i] not in dup:
            #dup[str(x[i])]=1
            #count+=1
            z.append(i)
        elif x[i] in dup:
            #dup[str(x[i])]= dup[str(x[i])]+1
            #count+=1
            z.append(i)
    return z

x=[1,1,2,4,2,3,1,1,3,2,1,1,"ac","Abc","ac","ac","Abc","ac"]
result=count_duplicate(x)

print("The duplicated elements located in the given indices\n",result)
