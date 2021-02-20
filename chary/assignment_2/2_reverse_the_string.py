#Write a program reverse a given input string

def reverse_string(x):
    y=""
    z=len(x)
    for i in range(-1,-(z+1),-1):
        y=y+x[i]
    return y


x=input("Enter the input string:")
output_string=reverse_string(x)

print(output_string)
