
#WAP count number of occurrences of vowels in a given string-

y=['Passion','Yearning','Transperancy','Humble','Achieve','Iron','Noble']
def vowels_count(y):
    count=0
    for i in y:
        for j in i:
            if j in "AEIOUaeiou":
                count=count+1
    return count
            
print(vowels_count(y))                


        
 #if Take Single For loop it take chr in each str  ****

        
    
