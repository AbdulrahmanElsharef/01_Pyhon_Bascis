# class Student():
#       student_info = {}
#       num_student_in = 0
#       default_student_age = range(1, 40)

#       @classmethod
#       def student_inclass(Student):
#            print(f"number of student in class is {Student.num_student_in}")

#       @classmethod
#       def student_inf(Student):
#            print(f"student_1 all information is {Student.student_info}")

#       @staticmethod
#       def welcom_class(school, cname, cnum):
#            print(
#                f"Wekcome in {school} school your class is{cname} : class({cnum})")

#       def __init__(self, name, age, subject):
#            self.__name = name
#             self.__age = age
#             self.__subject = subject
#             Student.num_student_in += 1
#             Student.student_info.update(
#                   {"student_name": self.__name, "student_Age": self.__age, "Student_subjects": self.__subject})

#       def get_name(self):
#            return self.__name

#       def set_name(self, new_name):
#            self.__name = new_name
#             Student.student_info.update({"student_name": new_name})

#       def get_age(self):
#            return self.__age

#       def set_age(self, new_age):
#            self.__age = new_age
#             Student.student_info.update({"student_Age": new_age})

#       def get_subject(self):
#            return self.__subject

#       def set_subjects(self, new_subject):
#            self.__subject = new_subject
#             Student.student_info.update({"Student_subjects": new_subject})

#       def chek_age(self):
#            if self.__age in Student.default_student_age:
#                  print("you are valid studen")
#             else:
#                  print("invalid student")


# student_1 = Student("hamada",45,["hg","ku"])
# student_1.welcom_class("salah salem", 'Math',"2/3")
# student_1.student_inf()
# student_1.set_name("abdo fawzy")
# student_1.set_age(38)
# student_1.set_subjects(["france", "math"])
# student_1.student_inf()
# student_1.student_inclass()
# student_1.chek_age()
# print("*"*50)

# student_2 = Student("MARWA", 25, {"France": 23,"ar":"exelent"})
# student_2.welcom_class("Atef Elsadat", 'Arabic', "1/6")
# student_2.student_inf()
# student_2.set_name("joud")
# student_2.set_age(3)
# student_2.set_subjects({"arab": 23, "eng": "accept"})
# student_2.student_inf()
# student_2.student_inclass()
# student_2.chek_age()
# print("*"*50)



from ast import Pass
from msilib.schema import Class


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