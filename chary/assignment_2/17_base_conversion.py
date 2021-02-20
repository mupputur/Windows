#Write a program convert base 10 to base 2 , base 8 , base 16 number systems.

def binary_conversion(b):
    y=""
    while(1):
        y=y+str((b%2))
        b=(b//2)
        if b==1:
            y=y+"1"
            b_result=y[-1:-(len(y)+1):-1]
            return b_result
        
def octal_conversion(o):
    y=""
    while(1):
        y=y+str((o%8))
        o=(o//8)
        if o>=1 and o<=7:
            y=y+str(o)
            octal_result=y[-1:-(len(y)+1):-1]
            return octal_result

def remainder(r):
    H={"10":'A',"11":'B',"12":'C',"13":'D',"14":'E',"15":'F'}
    if r<=9:
        return str(r)
    if r>9:
        return H[str(r)]


def hexa_conversion(h):
    y=""
    while(1): 
        r=h%16
        y=y+remainder(r)
        h = (h//16)
        if h==0:
            hexa_result=y[-1:-(len(y)+1):-1]
            return hexa_result    

    
for i in range(20):
    x=int(input("\nEnter the decimal number:"))
    print("\nIn binary:",binary_conversion(x),"\nIn octal:",octal_conversion(x),"\nIn Hexa:",hexa_conversion(x))    

