class Iphone():
     ''' new class of iphone '''
     serial=""
     def __init__(self,model,color,stor,cam):
          self.model=model
          self.color=color
          self.stor=stor
          self.cam=cam
     def prod(self,status,date):
          if status == "Stable":
               print(f"iphone model ({self.model}) is {status} Edition ")
               print(f"iphone model ({self.model})is Redy fo Selling At {date} ")
          else:
               print(f"iphone model ({self.model}) Is {status} Edition ")
               print(f"iphone model ({self.model})Is Unavilabe for Selling Befor {date} ")


class Iphone_X(Iphone):
     ''' new class of iphone '''
     Pass

print("_____________________________________________________\n")
p_serial=input("Enter Product Serial :")
p_model=input("Enter Product Model :")
p_color = input("Enter Product Color :")
p_storage = input("Enter Product Storage :")
p_camera = input("Enter Product Cam Mega :")
print("*******************************************************\n")

iphone_01 = Iphone(p_model, p_color, p_storage, p_camera)
iphone_01.serial = p_serial
print(f"iphone_01 serial is ({iphone_01.serial}) ")
print(f"iphone_01 model is ({iphone_01.model}) ")
print(f"iphone_01 color is ({iphone_01.color}) ")
print(f"iphone_01 storage is ({iphone_01.stor}) ")
print(f"iphone_01 cam is ({iphone_01.cam}) ")
iphone_01.prod("Stable", "31/12/2022")


print("_____________________________________________________\n") 
p_serial = input("Enter Product Serial :")
p_model = input("Enter Product Model :")
p_color = input("Enter Product Color :")
p_storage = input("Enter Product Storage :")
p_camera = input("Enter Product Cam Mega :")
print("*******************************************************\n")

iphone_X02 = Iphone_X(p_model, p_color, p_storage, p_camera)
iphone_X02.serial = p_serial
print(f"iphone_X02 serial is ({iphone_X02.serial}) ")
print(f"iphone_X02 model is ({iphone_X02.model}) ")
print(f"iphone_X02 color is ({iphone_X02.color}) ")
print(f"iphone_X02 storage is ({iphone_X02.stor}) ")
print(f"iphone_X02 cam is ({iphone_X02.cam}) ")
iphone_X02.prod("Beta", "31/6/2023")
print("_____________________________________________________\n")


'''
_____________________________________________________

Enter Product Serial :iph-2022-1400afg

iphone_01 serial is (iph-2022-1400afg)
iphone_01 model is (iphone-14)
iphone_01 color is (black)
iphone_01 storage is (128G)
iphone_01 cam is (148Mg)
iphone model (iphone-14) is Stable Edition
iphone model (iphone-14)is Redy fo Selling At 31/12/2022
_____________________________________________________

Enter Product Serial :iph-2023-xp0145ak
Enter Product Model :
Enter Product Color :Gray
Enter Product Storage :256G
Enter Product Cam Mega :156Mg
*******************************************************

iphone_X02 serial is (iph-2023-xp0145ak)
iphone_X02 model is ()
iphone_X02 color is (Gray)
iphone_X02 storage is (256G)
iphone_X02 cam is (156Mg)
iphone model () Is Beta Edition
iphone model ()Is Unavilabe for Selling Befor 31/6/2023
_____________________________________________________
'''
