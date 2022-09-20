#In Python a function is defined using the def keyword:

def my_function():
  print("Hello from a function")
  #To call a function, use the function name followed by parenthesis:
my_function()
#Information can be passed into functions as arguments.
def my_function(fname):
  print(fname + " elsharef")

my_function("abdo")
my_function("hamed")
#A parameter is the variable listed inside the parentheses in the function definition.

#An argument is the value that is sent to the function when it is called.
#By default, a function must be called with the correct number of arguments.
#Meaning that if your function expects 2 arguments,
#you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("abdo", "elsharef")
#If you try to call the function with 1 or 3 arguments, you will get an error:
#This function expects 2 arguments, but gets only 1:


#You can also send arguments with the key = value syntax.

#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "abdo", child2 = "nour", child3 = "zain")


#The following example shows how to use a default parameter value.

#If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("usa")
my_function("egypt")
my_function()
my_function("ksa")


#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

x=my_function(3)
print(x)
print(my_function(5))
print(my_function(9))
#A lambda function is a small anonymous function.
#The expression is executed and the result is returned:
#Lambda functions can take any number of arguments:

x = lambda a, b : a + b
print(x("abdo", "elsharef"))
