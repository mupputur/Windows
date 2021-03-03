
#Write a program reverse a given input string

def reverse_string(given_str):
    new_str=""
    for ch in given_str:
        new_str=ch+new_str
    return new_str

given_str=input("Enter the input string:")

print(reverse_string(given_str))
