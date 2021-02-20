#WAP to accept a grad & declare the equivalent description

def grade_description(grade):
    if(grade == "E"):
        print("Grade 'E' means 'Excellent'")
    elif(grade is "V"):
        print("Grade 'V' means 'Very Good'")
    elif(grade is "G"):
        print("Grade 'G' means 'Good'")
    elif(grade is "A"):
        print("Grade 'A' means 'Average'")
    elif(grade is "F"):
        print("Grade 'F' means 'Fail'")
    else:
        print("Please, enter valid 'Grade' as an input.")


print("Enter any one of the Grade from the below menu, to know the Description :")
print("E","V","G","A","F")
grade=input()
grade=grade.upper()
grade_description(grade)
