#Write a program reverse the given input list 

def list_reverse(x):
    new_list=[]
    for i in range(-1,-(len(x)+1),-1):
        new_list.append(x[i])
    return new_list

input_list=[1,2,3,4,5,'adfc',6,7,8,'chary',10]

reverse_output=list_reverse(input_list)
print(reverse_output)
