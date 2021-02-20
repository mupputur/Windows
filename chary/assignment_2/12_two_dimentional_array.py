#Write a program construct two dimensional array and print the same.
import random

def two_D_array(i,j):
    array=[[random.randint(0,20)]*j]*i
    return array

x=int(input("Enter the number of rows"))
y=int(input("Enter the number of coloumns"))

result=two_D_array(x,y)

print(result)
