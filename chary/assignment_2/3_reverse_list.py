#Write a program reverse the given input list 

def list_reverse(x):
    y=[]
    for i in range(-1,-(len(x)+1),-1):
        y.append(x[i])
    return y

x=[1,2,3,4,5,'adfc',6,7,8,'chary',10]

reverse_output=list_reverse(x)
print(reverse_output)
