#WAP to find the eligibility of admission for a professional course
#based on the following criteria:
def eligibility_for_admission(m,p,c,total):
    if (m>=65 and p>=55 and c>=50 and total>=180):
        print("The candidate is Eligible for the 'Admission'")
    elif(m+p)>=140:
        print("The candidate is Eligible for the 'Admission'")
    else:
        print("The candidate is 'Not Eligible' for the 'Admission'")

for i in range(5):
    print("\nEnter the Marks details, to find the Eligibility for admission")
    m=int(input("Enter the Marks in Mathematics :"))
    p=int(input("Enter the Marks in Physics     :"))
    c=int(input("Enter the Marks in Cemistry    :"))
    total=(m+p+c)
    eligibility_for_admission(m,p,c,total)
