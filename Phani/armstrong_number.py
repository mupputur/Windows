#Write a program find a given number is Armstrong or not
def armstrong_number(num):
    len_num=len(str(num))
    sum=0
    y=num
    while y!=0:
        rem=y%10
        sum+=rem**len_num
        y=int(y/10)
    if num==sum:
        return("its a armstrong number")
    else:
        return("its not a armstrong number")
print(armstrong_number(int(input("enter number"))))
