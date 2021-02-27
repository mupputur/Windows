#wap to reverse a given list
def reverse_list(list):
    for num in range(len(list)//2):
        list[num],list[len(list)-num-1]= list[len(list)-num-1], list[num]
    return list    
list=eval(input("enter the elements in list format:"))
print(reverse_list(list))
