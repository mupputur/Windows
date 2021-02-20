#Write a program print longest length string from given input list of strings.

def longest_length_string(x):
    long_str=len(x[0])
    for i in range(len(x)):
        if long_str<len(x[i]):
           long_str=len(x[i])
           y=x[i]
    return y




x=[]
for i in range(5):
    x.append(str(input("enter the string: ")))
print("The given list is",x)
print("\nThe longest sting, withing the list is:\n",longest_length_string(x))
