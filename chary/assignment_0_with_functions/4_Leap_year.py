#WAP TO FIND WHETHER A GIVEN YEAR IS A LEAP YEAR OR NOT by using functions
"""def leap_year(x):
    if x%100==0:
        if x%400==0:
            print("The given year is a leap year")
        else:
            print("The given year is a 'Non-leap year'")
    elif x%4==0:
        print("The given year is a leap year")

    elif x%4!=0:
        print("The given year is a 'Non-leap year'")
"""
def leap_year(x):
    if x%100==0 and x%400==0:
        return 1
    elif x%100!=0 and x%4==0:
        return -1

for i in range(3):
    x=(int(input("Enter the year: ")))

    result=leap_year(x)

    if result==1:
        print("The given year is a leap year")
    elif result==-1:
        print("The given year is a leap year")
    elif result==None:
        print("The given year is a 'Non-leap year'")







        
    
