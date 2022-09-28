2<3
True
5>6
False
#  == is equal
# != not equal
# < greeter than
# < less than
# > greater than
#<= less than or equal to
#<= less than or equal to
#It is even possible to combine these operators.
x=20
5<x<50
True
10<x<15
False
#The conditional operators work even on strings
"abdulrahman">"abdo"
True
"abdo" != "elsharef"
True
"abdo" > "elsharef"
False
#There are few logical operators to combine boolean values.
#• x and y is True only if both a and b are True.
#• a or b is True if either a or b is True.
#• not x is True only if x is False
True and True
True
True or False
True
2 < 3 and 3 > 1
True
2 < 3 or 3 > 1
True
2 < 3 and not 3 > 1
False
x=5
y=12
p = x < y or x < z
p
True
x=50
if x % 2 == 0:
      print ('even')
      
x = 3
if x % 2 == 0:
      print ('even')
else:
      print ('odd')
     # Problem 17: What happens when the following code is executed? Will it give any error? Explain the reasons.
x = 2
if x == 2:
      print (x)
else:
      print (y)
     # Will not give any error
     #Problem 18: What happens the following code is executed? Will it give any error? Explain the reasons.
x = 2
if x == 2:
      print(x)
#else:
     # x +
      #Will  give  error fo invalid syntax in else we have make code x+=2

#If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
# If statement, without indentation (will raise an error)
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#This technique is known as Ternary Operators, or Conditional Expressions.
print("A") if a > b else print("B")
#Test if a is greater than b, and if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#You can have if statements inside if statements, this is called nested if statements.

#Example
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
