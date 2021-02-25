#Write a program find a given number is Armstrong or not
def armstrong_number(x):
    sum=0
    y=x
    while y!=0:
        num=y%10
        sum+=num**3
        y=int(y/10)
    print(sum)
    if x==sum:
        return("its a armstrong number")
    else:
        return("its not a armstrong number")
print(armstrong_number(int(input("enter number"))))
