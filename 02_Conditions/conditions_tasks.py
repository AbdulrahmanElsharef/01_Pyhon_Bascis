x=10
if x>15:
      print("true")
else:
      print("x is smaller than 15")
# _____________________________________
# we use all in case we need all conditions true
# _______________________________________
# diffrence between all & "and" is all when we need all conditions true
#  "and" is logical opreator to Returns True if both statements are true
# _________________________________________________________
#  if we need all conditions true we use "and"
# ___________________________________________________________________
# diffrence between if & elif is 
# "if" is the first and hole conditon
# "elif" when if statment is false then i need another conditons is by using "elif"
# ___________________________________________________________________________
# diffrence between elif & else is
# "elif" when if statment is false then i need another conditons is by using "elif"
# "else" when all conditions notcatches anything do this code
# ___________________________________________________________
# can we use more "elif"
# yes we can use it alot of times
# __________________________________________________
# can we use more "else"
# no we use it at the end of statment
# __________________________________________________
# in "elif" we use "else" for if nothing is true
# _______________________________________________________________
abd_lis=[2,6,4,8,10]
if 4 in abd_lis:
      print("4 in list")
      if 4 and 6 in abd_lis:
            print("4 & 6 in list")
else:
      print("number not in list")
# ____________________________

if 3 or 6 in abd_lis:
      print ("3 or 6 in list")
else:
      print("number not in list")
#___________________________ ____________________
if 2 and 4 and 5 in abd_lis:
      print("2 & 4 & 5 in list")
else:
      print("number not in list")
