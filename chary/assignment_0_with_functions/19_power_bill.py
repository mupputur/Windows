#WAP to calculate and print the electricity bill of a given customer.
#The Customer id,Name & unit consumed by the user should be taken form
#the Keyboard & display the total amount to pay to the customer.
def power_bill(u):
    if (0<=u and u<200):
        print("The Electricity bill is Rs : ",u*1.20)
    elif(200<=u and u<400):
        print("The Electricity bill is Rs: ",u*1.50)
    elif(400<=u and u<600):
        print("The Electricity bill is Rs: ",u*1.80)
    elif(u>=600):
        print("The Electricity bill is Rs: ",u*2.0)
    else:
        print("Enter the number of units properly")


for i in range(5):
    c_id=input("\nEnter the customer id:")
    c_name=input("Enter the Name:")
    no_of_u=float(input("Enter number of units consumed: "))
    print("Cuntomer id is: ",c_id)
    print("Cuntomer name is: ",c_name)
    power_bill(no_of_u)
    
