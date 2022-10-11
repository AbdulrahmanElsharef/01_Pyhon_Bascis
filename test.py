'''def dis(p, d):
      price=int(p)
      dis=int(d)/100
      net_price=(price*dis)
      print(round(net_price,4))
dis(1500, 50)
# 750.0
dis(89, 20)
# 17.8
dis(100, 75)
# 75.0 '''                                                            .py"






# Arrays can be mixed with various types. Your task for this challenge is to sum all the number elements in the given array. Create a function that takes an array and returns the sum of all numbers in the array.
'''def numbersSum(l):
      lis=l
      sum=0
      for x in lis:
            if type(x) == int:
                  sum += x
            elif type(x)== str:
                  y=int(x)
                  sum+=y
            else:
                  pass
      print(f"sum of list = {sum}")
numbersSum([1, 2, "13", "4", "645"])
# sum of list = 665
numbersSum([True, False, "123", "75"])
# sum of list = 198
numbersSum([1, 2, 3, 4, 5, True])
# sum of list = 15'''




# You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find Nemo]!".
# If you can't find Nemo, return "I can't find Nemo :(".
'''def findNemo(s):
      x=str(s).split(" ")
      y = x.index("Nemo")+1
      print(f'"I found Nemo at {y}!"')


findNemo("I am finding Nemo !")
# "I found Nemo at 4!"
findNemo("Nemo is me") 
# "I found Nemo at 1!"
findNemo("I Nemo am") 
# "I found Nemo at 2!"'''
