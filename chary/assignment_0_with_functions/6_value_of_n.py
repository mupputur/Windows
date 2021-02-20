#WAP TO READ THE VALUE OF AN INTEGER m & DISPLAY THE VALUE OF n IS 1
#WHEN M IS LARGER THAN 0,0 WHEN m IS 0 & -1 WHEN m IS LESS THAN 0 BY
#USING FUNCTIONS

def value_of_n(m):
    if m>0:
        return 1
    elif m==0:
        return 0
    else:
        return -1


print("Enter the intiger value of 'm' :")
m=int(input())

result=value_of_n(m)
print("The value of n is:",result)
