#Write a program print longest length string from given input list of strings

def long_string(strings):
    max=0
    for string in strings:
        if len(string) > max:
            max=len(string)
            long_string=string
    return long_string
strings=["phani","phaneendra","jahanavi","chary","suresh","praksh","brahmacharyulu","a"]
print(long_string(strings))

