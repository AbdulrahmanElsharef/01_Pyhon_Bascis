# '''def dis(p, d):
#       price=int(p)
#       dis=int(d)/100
#       net_price=(price*dis)
#       print(round(net_price,4))
# dis(1500, 50)
# # 750.0
# dis(89, 20)
# # 17.8
# dis(100, 75)
# # 75.0 '''                                                            .py"


# # Arrays can be mixed with various types. Your task for this challenge is to sum all the number elements in the given array. Create a function that takes an array and returns the sum of all numbers in the array.
# '''def numbersSum(l):
#       lis=l
#       sum=0
#       for x in lis:
#             if type(x) == int:
#                   sum += x
#             elif type(x)== str:
#                   y=int(x)
#                   sum+=y
#             else:
#                   pass
#       print(f"sum of list = {sum}")
# numbersSum([1, 2, "13", "4", "645"])
# # sum of list = 665
# numbersSum([True, False, "123", "75"])
# # sum of list = 198
# numbersSum([1, 2, 3, 4, 5, True])
# # sum of list = 15'''


# # You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find Nemo]!".
# # If you can't find Nemo, return "I can't find Nemo :(".
# '''def findNemo(s):
#       x=str(s).split(" ")
#       y = x.index("Nemo")+1
#       print(f'"I found Nemo at {y}!"')


# findNemo("I am finding Nemo !")
# # "I found Nemo at 4!"
# findNemo("Nemo is me")
# # "I found Nemo at 1!"
# findNemo("I Nemo am")
# # "I found Nemo at 2!"'''


'''def compareTriplets(a, b):
      # lis1=list(a)
      # lis2=list(b)
      lis3=[]
      alice=0
      bob=0
      for x, y in zip(a, b):
            if x>y:
                  alice+=1
            elif x<y:
                  bob+=1
      lis3.append(alice)
      lis3.append(bob)
      return(lis3)

a=[17,28,30]
b = [99, 16, 8]

compareTriplets(a,b)'''


'''def bonAppetit(bill, k, b):
      lis=list(bill)
      lis.pop(k)
      rest =sum(lis)
      split = rest/2
      if b > split:
            new_b = b-split
            print(int(new_b))
      elif b <= split:
            print("Bon Appetit")


n,k=4,1
bill=[3,10,2,9]
b = 15
bonAppetit(bill, k, b)'''


'''def coneVolume(h,r):
      n=22/7
      volum=(1/3)*n*(r**2)*h
      return round(volum,2)
res = coneVolume(18,0)
print(res)'''


'''def areaOfCountry(name,area):
      total_world = 148940000
      country_area = (area/total_world)*100
      res=round(country_area,2)
      print(f"{name} is {res} % of the total world's landmass")
areaOfCountry("Russia", 17098242)'''


'''def reverseWords(string):
      str(string).rstrip()
      lis=list(string.split(" "))
      # x=lis.pop()
      
      print(lis)


reverseWords(" the sky is blue")
# s=" the sky is blue"
# s.strip()
# x=list (s.split(" "))
# print(x)'''


# Create a function that moves all capital letters to the front of a word

'''def capToFront(string):
      cstr=""
      sdtr=""
      for x in str (string):
            if x==x.upper():
                  cstr=cstr+x
            else:
                  sdtr = sdtr+x
      print(cstr+sdtr)


capToFront("hApPy")
# APhpy
capToFront("moveMENT") 
# MENTmove
capToFront("shOrtCAKE")
# OCAKEshrt'''


# Mubashir was reading about currying functions. He needs your help to multiply an array of numbers using currying functions.

# Create a function which takes a array arr of integers as an argument. This function must return another function, which takes a single integer as an argument and returns a new array.

# The returned array should consist of each of the elements from the first array multiplied by the integer.
'''def fun(n):
      return n
def multiply(arr,mult):
      mult=fun(num)
      new_lis=[]
      for x in arr:
            x=x*mult
            new_lis.append(x)
      print(new_lis)

num = int(input("enter num "))
multiply([4, 6, 5],num)'''


'''def numInStr(arr):
      lis=[]
      for x  in arr:
            if str(x).isalpha() == False:
                  lis.append(x)
            else:
                  pass
      print( lis)


# ['1a', '2b']
numInStr(["1a", "a", "2b", "b"])
# ['abc10']
numInStr(["abc", "abc10"])
# ['ab10c', 'a10bc']
numInStr(["abc", "ab10c", "a10bc", "bcd"])'''


'''def fizz_buzz(n):
      if n %3 ==0 :
            print("Fizz")
      elif n % 5 == 0:
            print("Buzz")
      elif n %5 ==0 and n%3 ==0:
            print("FizzBuzz")
      elif n % 5 != 0 or n % 3 != 0:
            print(str(n))


fizz_buzz(3) #➞ "Fizz"

fizz_buzz(5) #➞ "Buzz"
''
fizz_buzz(15) #➞ "FizzBuzz"

fizz_buzz(4) #➞ "4'''

# _________________________________________________________________
'''def libraryFine(d1, m1, y1, d2, m2, y2):
      if y1>y2:
            fine = 10000
            return fine
      elif y1 == y2:
            if m1 > m2:
                  hackos=500
                  fine = hackos*(m1-m2)
                  return fine
            elif m1 == m2:
                  if d1>d2:
                        hackos = 15
                        fine = hackos*(d1-d2)
                        return fine
                  else:
                        fine=0
                        return fine
            else:
                  fine = 0
                  return fine
      else:
            fine=0
            return fine

print(libraryFine(d1, m1, y1, d2, m2, y2))'''


'''def word(w):
      lis=[]
      word=str(w)
      for y in word :
            lis.append(y)
      lis.sort()
      print(lis)
      new="".join(lis)
      if new > word:
            print(new)
      else:
            print(new)'''


'''word("fedcbabcd")'''
# fruits_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruits_list.sort()
# print(neww)


# import math
# def gradingStudents(grades):
#     lis = []
#     for x in range(grades):
#         num5 = math.ceil(grades[x]/5)
#         new_g = num5*5
#         if grades[x] >= 38:
#             if new_g-grades[x] < 3:
#                 lis.append(new_g)
#             elif new_g-grades[x] >= 3:
#                 lis.append(grades[x])
#         elif grades[x] < 38:
#             lis.append(grades[x])


# gradingStudents(4)
# gradingStudents(73)
# gradingStudents(67)
# gradingStudents(38)
# gradingStudents(33)

# print("finish")


'''This quarterly scheme is calculated with a threshold target of 32 days per quarter, and the incentive payment for each billable day in excess of such threshold target is shown as follows:

Days	Bonus
0 to 32 days	Zero
33 to 40 days	SGD$325 per billable day
41 to 48 days	SGD$550 per billable day
Greater than 48 days	SGD$600 per billable day
Please note that incentive payment is calculated progressively. As an example, if an employee reached total billable days of 45 in a quarter, his/her incentive payment is computed as follows:'''


'''def bonus(n):
      if n >0 and n <=32 :
            print (f"bouns is {0} $")
      elif n >32 and n <=40:
            x=n-32
            bon=x*325
            print (f"bouns is {bon} $")
      elif n >40 and n <=48:
            x=8*325
            y=(n-40)*550
            bon = x+y
            print (f"bouns is {bon} $")
      else:
            x=8*325
            y=8*550
            z=(n-48)*600
            bon=x+y+z
            print (f"bouns is {bon} $")
            
            
bonus(15) #➞ 0
bonus(37) #➞ 1625
bonus(43)
bonus(50) #➞ 8200'''


# def count_datatypes(*data):
#       lis=[]
#       # lis_d=list(date)
#       order_lis=[int, str, bool, list, tuple, dict]
#       # for x in order_lis:
#       for y in data:
#             if type(y) in order_lis:
#                   lis.append(data.count(type(y)))
#             elif type(y) not in order_lis:
#                   lis.append(0)
#       return lis
# print(count_datatypes(1, 45, "Hi", False))


# def simpleArraySum(*ar):
#       # lis=list(ar)
#       sum = 0
#       for x in ar:
#             sum += x
#       return sum
# print(simpleArraySum(1000000001 ,1000000002 ,1000000003 ,1000000004 ,1000000005))


# # from datetime import date
# class player():
#     def __init__(self, name, age, height, weight):
#         self.age = int(age)
#         self.name = str(name)
#         self.height = int(height)
#         self.weight = int(weight)

#     def get_age(self):
#         print(f'{self.name} is age {self.age}'.title())

#     def get_height(self):
#         print(f'{self.name} is  {self.height} cm'.title())

#     def get_weight(self):
#         print(f'{self.name} is age {self.weight} kg'.title())


# p1 = player("abd", 33, 172, 78)
# p1.get_age()
# p1.get_height()
# p1.get_weight()

# # helllloooooooooooooooooooooo


'''class Employee():
      def __init__(self,firstname ,lastname ):
            self.firstname=str(firstname)
            self.last=str(lastname)
            self.fullname =f"{self.firstname} {self.last}"
            self.email=f"{self.firstname}.{self.last}@company.com" 


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
print(emp_1.fullname) #➞ "John Smith"

print(emp_2.email) #➞ "mary.sue@company.com"

print(emp_3.firstname) #➞ "Antony"'''


'''class num():
      def __init__(self) :
            self.ones=0
            self.threes=0
            self.nines=0
      def ones_threes_nines(self,n):
            self.ones=int(n/1)
            self.threes=int(n/3)
            self.nines=int(n/9)
            return self.ones,self.threes,self.nines
n1=num()            
n1 . ones_threes_nines(5)
print(n1.nines) #➞ 0

print(n1.ones) #➞ 5

print(n1.threes) #➞ 1'''


'''def dna_to_rna(string):
      list_word = list(string)
      new_word = []
      for x in list_word:
            if x == "A":
                  new_word.append("U")
            elif x == "T":
                  new_word.append("A")
            elif x == "G":
                  new_word.append("C")
            elif x == "C":
                  new_word.append("G")
      print("".join(new_word))


dna_to_rna("ATTAGCGCGATATACGCGTAC") #➞ "UAAUCGCGCUAUAUGCGCAUG"

dna_to_rna("CGATATA") #➞ "GCUAUAU"

dna_to_rna("GTCATACGACGTA") #➞ "CAGUAUGCUGCAU"

'''


'''def vowel_links(string):
    word = string.split(" ")
    tex1 = ""
    tex2 = ""
    for x in word:
        if str(x).startswith()


vowel_links("a very large appliance")'''

from tomlkit import array

lis=[12,12,65,36,78,21]
def sum_lis(*aray):
      '''function to sum all of list items
      for x in list:
            x=item  #[from list]
            sum+=x
      end func
      '''
      pass
result=sum(lis)
# print(result)
help(sum_lis)

