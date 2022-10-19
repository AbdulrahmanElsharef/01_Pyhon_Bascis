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

#_________________________________________________________________
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



x="hello new pc"
print(x)
