#variables
a = 5 
print(type(a)) #int

a = "ujjwal"
print(type(a)) #str

a = 2 + 4j
print(type(a))  #complex

a = 4.0
print(type(a))  #float

# redeclaring the var
age = 23
salary = 1234.5
name = "Mark"
# display
print(age)  #23
print(salary)  #1234.5
print(name) #mark

#Assigning a single value to multiple variables:
a = b = c = 10
print(a)  #10
print(b) #10
print(c) #10

#Assigning different values to multiple variables:
a, b, c = 1, 20.2, "Python"

print(a) #1
print(b) #20.0
print(c) #python

#Can we use the same name for different types?
a = 10
a = "Python"
print(a)  #python

#How does + operator work with variables?
a = 10
b = 20
print(a+b)  #30
a = "Python"
b = "Django"
print(a+b)  #pythonDjango

#Can we use + for different types also?
# a = 10
# b = "Python"
# print(a+b) #error

a = 3
b = a
c = a
a = "hello"
print(a)
print(b)
print(c) 

#input
# name = input("enter your name : ")
# print("hello " + name)  #hello ujjwal

#integer input nin python
# n = int(input("enter a number : "))
# print(n) 
# print(type(n)) #int

#Python String formatting using F string and format()
a = "Hello"
b = "World"
print(a,b)  #hello world
print('{} {}'.format(a,b)) #hello world
print(f"{a} {b}") #hello world

a = 1
b = 2
print('The value of a is {0} and b is {1}'.format(a,b)) #The value of a is 1 and b is 2
print(f'The value of a is {a} and b is {b}') #The value of a is 1 and b is 2

#data types
# Numeric (int,float)

a = 5
print("Type of a: ", type(a)) #Type of a:  <class 'int'>
b = 5.0
print("\nType of b: ", type(b))  #Type of b:  <class 'float'>
c = 2 + 4j
print("\nType of c: ", type(c)) #Type of b:  <class 'complex'>

# Sequence(string,list,tuple)
# string
#sequence data types
#string
#creating a string
s = 'python'
s1 = "python"
s2 = '''python'''
s3 = """python"""
print(s) #python
print(s1) #python
print(s2) #python
print(s3) #python

#Accessing elements of String
s = "python"
print(s[0]) #p
print(s[-1]) #n

#list
l = [1,2,3,4,5]
print(l) #[1,2,3,4,5]
print(l[0]) #1
print(l[-1]) #5
print(type(l)) #<class 'list'>

# tuple

t = (1,2,3,4,5)
print(t) # (1,2,3,4,5)
print(t[0]) #1
print(t[-1]) #5
print(type(t)) #<class 'tuple'>

# Boolean
a = True
b = False
print(a) #true
print(b) #false
print(type(a)) #boolean
print(type(b)) #boolean

# Set
s = {1,2,3,4,5,5}
print(s)
print(type(s)) #set
#print(s[0])
# for i in s:
#   print(i)

# Dictionary
d = {'a':1,'b':2,'c':3}
print(d)
print(d['a']) #1
print(d['b']) #2
print(d['c']) #3
print(type(d)) #dict
print(d.get('a')) #1
print(d.get('d')) #none

# Type conversion
x = 10
print("x is of type:",type(x)) #x is of type: <class 'int'>
y = 10.6
print("y is of type:",type(y)) #y is of type: <class 'float'>
x = x + y #20.6
print(x)
print("x is of type:",type(x))  #x is of type: <class 'float'>

#Operators
# 1. arithmetic operator
# Examples of Arithmetic Operator
a = 4
b = 5
# Addition of numbers
add = a + b
# Subtraction of numbers
sub = a - b
# Multiplication of number
mul = a * b
# Division(float) of number
div1 = a / b
# Division(floor) of number
div2 = a // b
# Modulo of both number
mod = a % b
# Power
p = a ** b
# print results
print(add) #9
print(sub)#-1
print(mul)#20
print(div1)#0.8
print(div2)#0
print(mod)#4
print(p)#1024

# 2. Comparison operators (relational operators)

# Examples of Relational Operators
a = 13
b = 33
# a > b is False
print(a > b)
# a < b is True
print(a < b)
# a == b is False
print(a == b)
# a != b is True
print(a != b)
# a >= b is False
print(a >= b)
# a <= b is True
print(a <= b)

# 3.Logical Operators
# Examples of Logical Operator
a = True
b = False
# Print a and b is False
print(a and b)
# Print a or b is True
print(a or b)
# Print not a is False
print(not a)

# 4. Assignment Operators
# Examples of Assignment Operators
a = 10
# Assign value
b = a
print(b) #10
# Add and assign value
b += a
print(b) #20
# Subtract and assign value
b -= a
print(b) #10
# multiply and assign
b *= a
print(b) #100

# 5. Identity Operators (is and is not)
a = 10
b = 20
c = a
d = 10
print(a is b) #false
print(a is not b) #true
print(a is c) #true
print(a is d) #true

# 6. Membership Operators (in and not in)
# Python program to illustrate
# not 'in' operator
x = 24
y = 20

list = [10, 20, 30, 40, 50]
if (x not in list):
    print("x is NOT present in given list") #x is NOT present in given list
else:
    print("x is present in given list")
if (y in list):
    print("y is present in given list") #y is present in given list
else:
    print("y is NOT present in given list")

expr = 10 + 20 * 30
print(expr)
# Precedence of 'or' & 'and'
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
   print("Hello! Welcome.")
else:
    print("Good Bye!!")