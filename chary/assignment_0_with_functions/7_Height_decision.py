"""wap to accept the height of a person in "cm" & categorize the person according
   to their height. if the height is less than 150 cm, display o/p as "DWARF"
   & if the height is greater than equal to 150 and less than 165 cm , display as
   "AVERAGE HEIGHT" and if the height is greater than 165 cm , display as "TALL".
"""
def Height_decision(cm):
    if cm<150:
        print('"DRARF"')
    elif cm>=150 and cm<=165:
        print('"AVERAGE HEIGHT"')
    elif cm>165:
        print('"TALL"')


cm=int(input("Enter the Height in 'cm' :"))
Height_decision(cm)
