#WAP to read any Month Number in integer and
#display the number of days i for this Month
def months_days(month):
    d=("JAN 31 days","Feb 28 days ","MAR 31 days","APR 30 days","MAY 31 days ","JUN 30 days","JUL 31 days","AUG 31 days","SEP 30 days","OCT 31 days","NOV 30 days","DEC 31 days")
    if(month>0 and month<=12):
        j=month
        print(d[j-1])
    else:
        print("Enter valid Number")



for i in range(12):
    m=int(input("Enter an integer value:"))
    months_days(m)
