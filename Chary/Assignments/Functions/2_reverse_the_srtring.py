#Write a program reverse a given input string

def reverse_string(given_str):
    new_str=""
    for i in range(-1,-(len(x)+1),-1):
        new_str=new_str+x[i]
    return new_str

given_str=input("Enter the input string:")
output_string=reverse_string(given_str)

print(output_string)
