print "hello, world!"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
print ("hello, world!")
hello, world!
x=4
x*x
16
foo
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    foo
NameError: name 'foo' is not defined
foo=15
foo
15
x=220
x="abddo15"
x
'abddo15'
#f you re-assign a different value to an existing variable, the new value overwrites the old value.
#It is possible to do multiple assignments at once#
a,b,c=12,50,"abdo"
a
12
b
50
c
'abdo'
#What will be output of the following program
x=20
y=x+30
x=2
x
2
y
50
#What will be the output of the following program.
x, y = 2, 6
x, y = y, x + 2
#x is 4 , y is 8
SyntaxError: multiple statements found while compiling a single statement
x
2
y
50
x,y=10,20
x,y=y+x+2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x,y=y+x+2
TypeError: cannot unpack non-iterable int object
7+2
9
50-20
30
10*3
30
500/4
125.0
#divition output is float
150//2
75
#floor divition is int
122/8%
SyntaxError: invalid syntax
122%8
2
5+6-4*2
3
'''It is important to understand how these compound expressions are evaluated. The operators have precedence, a
kind of priority that determines which operator is applied first. Among the numerical operators, the precedence of
operators is as follows, from low precedence to high.'''
'It is important to understand how these compound expressions are evaluated. The operators have precedence, a\nkind of priority that determines which operator is applied first. Among the numerical operators, the precedence of\noperators is as follows, from low precedence to high.'
#We can use parenthesis to specify the explicit groups.
(2 + 3) * 4
20
#Strings are a sequence of characters, enclosed in single quotes or double quotes.
x = "hello"
y = 'world'
SyntaxError: multiple statements found while compiling a single statement
x,y
(10, 20)
(10, 20)
(10, 20)
x="heelo"
y='world'
x,y
('heelo', 'world')
x = """This is a multi-line string
written in
three lines."""
x
'This is a multi-line string\nwritten in\nthree lines.'
y = '''multi-line strings can be written
using three single quote characters as well.
The string can contain 'single quotes' or "double quotes"
in side it.'''
#f you want to specify the data type of a variable, this can be done with casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y)
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
     # Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a

      #Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
     # Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
#You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z =  x + y
print(z)
      #If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
print(x + y)
 x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
#Setting the Specific Data Type
#If you want to specify the data type, you can use the following constructor functions:

#Example	Data Type	Try it
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = bool(5)	bool	

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'      

#The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
   #   The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

