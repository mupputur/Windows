# WAP FIND LARGEST OF TWO NUMBERS BY USING FUNCTIONS


def largest_number(x):
    max_no=x[0]
    for i in range(len(x)):
        if x[i]>max_no:
            max_no=x[i]
    return max_no

#no_of_ele=int(input("HOW MANY NUMBER OF INTEGERS YOU WANT TO PLACE IN LIST: "))
no_of_ele=2
x=[]
for i in range(no_of_ele):
    x.append(int(input("Enter the integer value : ")))
print("The list of elements you Entered is :",x)
maximum_num=largest_number(x)
print("The maximum number with in the given numbers is: ",maximum_num)
