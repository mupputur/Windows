#WAP to read any day number in integer and display day name in the word

def months_their_days(day):
    weeks=("MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY")
    if(day>0 and day<=7):
        j=day
        print(weeks[j-1])
    else:
        print("\nEnter valid Number")


for i in range(7):
    day=int(input("Enter an integer value:"))
    months_their_days(day)
