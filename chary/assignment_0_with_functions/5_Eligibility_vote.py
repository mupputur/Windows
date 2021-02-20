#WAP TO READ THE AGE OF A CANDIDATE &
#DETERMINE WHETHER IT IS EALIGIBLE FOR CASTING HIS/HER OWN VOTE by using functions

def eligibility(age):
    if(age>18):
        return "YOUR ARE 'ELIGIBLE' FOR CASTING VOTE"
    else:
        return "YOUR ARE 'NOT ELIGIBLE' FOR CASTING VOTE"


print("Enter the AGE :")
age=int(input())

eligibility(age)
print(eligibility(age))
