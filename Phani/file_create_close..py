#wap to create a file in desktop and delete the same file and check the
#file is in desktop or not and also check in recyclebin
import os

#creating new text file on desktop
path='C:\\Users\\Lenovo\\Desktop\\phani.txt'
f=open(path,"w")
mesg='im learning python prgraming at kondapi under the guidance of sai'
f.write(mesg)
f.close()

#checking the created file is in desktop or not
if os.path.isfile("C:\\Users\\Lenovo\\Desktop\\phani.txt"):
    print("file exist in desktop")
else:
    print("file not in desktop exist")
    
#delete the created text file    
os.remove("C:\\Users\\Lenovo\\Desktop\\phani.txt")
print("file deleted from desktop")

#checking the created file is in desktop or not
if os.path.isfile("C:\\Users\\Lenovo\\Desktop\\phani.txt"):
    print("file exist in desktop")
else:
    print("file not exist in desktop")
    
#checking the created file is in recycle bin or not
if os.path.isfile("D:\\$Recycle.Bin\\File_Content.txt"):
    print("file exist in recyclebin")
else:
    print("file not exist in recyclebin")
