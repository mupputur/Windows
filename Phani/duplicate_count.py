#Write a program count duplicated elements in the list
def duplicate_count(list):
    y={}
    z={}
    count=0
    for num in list:
        if num not in y:
            y[num]=1
        else:
            count=count+1
            z[num]=y[num]+1
    return count
list=[10,34,20,10,34,67,20]
print(duplicate_count(list))
            
        
