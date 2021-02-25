#Write a program print longest length string from given input list of strings

def long_string(x):
    max=0
    for i in x:
        if len(i) > max:
            max=len(i)
            y=i
    return y
x=["phani","phaneendra","jahanavi","chary","suresh","praksh","brahmacharyulu","a"]
print(long_string(x))




"""
    y=len(x[0])
    for i in range(1,len(x)):
        if len(x[i])>y :
            y=len(x[i])
"""

"""
def max_in_list(x):
    y=len(x[0])
    for i in range(1,len(x)):
        if y<len(x[i]):
            y=len(x[i])
            return x[i]

"""
