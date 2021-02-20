#WAP TO CALCULATE PROFIT AND LOSS ON A TRANSACTION FROM THE GIVEN COST
#PRICE(CP) AND SELLING PRICE (SP) BY USING FUNCTIONS
def profit_or_loss(cp,sp):
    if(cp<sp):
        print("Your 'profit' amount is :", sp-cp)
    elif(cp>sp):
       print("Your 'Loss' amount is :",cp-sp)
    else:
        print("Your are having 'No profit' & 'No Loss'")

print("Enter the COST PRICE (CP) :")
cp=int(input())
print("Enter the SELLING PRICE (SP) :")
sp=int(input())

profit_or_loss(cp,sp)
