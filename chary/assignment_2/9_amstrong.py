#Write a program find a given number is Armstrong or not?

def is_amstrong(x):
    l=len(str(x))
    y=str(x)
    mul_val=0
    for i in range(l):
        mul_val=mul_val+int(y[i])**l
    if mul_val==x:
        return True
    else:
        return False
                        # by using "%" operator also we can extract the digit 

x=int(input("Enter the number to find amstrong or not:"))
result = is_amstrong(x)

if result:
    print("Amstrong Number")
elif not result:
    print("Not an Amstrong Number")
