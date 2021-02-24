#Write a program find a given number is Armstrong or not?

def is_amstrong(num):
    len_of_num=len(str(num))
    mul_val=0
    temp_no=num
    while(num!=0):
        unit=num%10
        mul_val=mul_val+unit**len_of_num
        num=num//10
    if mul_val==temp_no:
        return True
    else:
        return False
                       
num=int(input("Enter the number to find amstrong or not:"))
result = is_amstrong(num)

if result:
    print("Amstrong Number")
elif not result:
    print("Not an Amstrong Number")
