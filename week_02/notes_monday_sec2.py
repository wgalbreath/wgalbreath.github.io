''' this is a triple quote (everything after should get ignored)
# anything that begins with a # is a comment
# comments are code that doesn't get executed

print('hello world')
print('goodbye world')

var1 = 'hello'
var2 = 'world'
var3 = var1 + ' ' + var2
print (var3)


# for integers, python is always going to give you exact results
# there are no size limits
# the type of a number with no period is called an int
x = 1  
y = 5
z = 5**999 # 5 raised to the power of 999
print(z)

# for non-integer numbers; (fractions, irrational numbers) are approximations - don't get exact answers
# type of a number with a period is called a float
x = 0.1
y = 0.1
z = 0.1
q = x + y + z

print (q)

# the last type is the str = "string" type, for strings

# python is an untyped "language" (CAN change the type of variable whenever we want)
# java is a strongly typed language (CANNOT change the variable after it has been declared)
x = 'this is a string'
print(x)

# import= keyword (shows up in purple); math= package/library that we are importing
import math
#pseudocode for the quatric formula
# (a**2 +- sqrt(b - 4ac)) / 2a
a = 5
b= 100
c = 2
quadratic1 = (a**2 + math.sqrt(b - 4 * a * c)) / (2 * a)
quadratic2 = (a**2 - math.sqrt(b - 4 * a * c)) / (2 * a)
print (quadratic1)
print (quadratic2)

a = 3 # need to redefine the equation below because python just reads top to bottom
quadratic1 = (a**2 + math.sqrt(b - 4 * a * c)) / (2 * a)
quadratic2 = (a**2 - math.sqrt(b - 4 * a * c)) / (2 * a)
print (quadratic1)
print (quadratic2)

# a*x**2 + b*x + c = 0 -- python is able to solve this but it is complicated

# functions + variables together are hte key difference between HTML/CSS (which don't have either of those) and Python (which do)
# def: define a function ; when you want to use a function again, you use this outline/formula:
def quadratic(a, b, c):
    result (a**2      - math.sqrt(b-4 * a * c)) / (2 * a) 
    # don't want to use print (result); doesn't let you use the value
    # print (result)
    return result # when you return your result, you can do further math or print it afterward so use RETURN RESULT

print (quadratic(5, 100, 2))
print (quadratic(3, 100, 2))
'''

x = 5
y = 7 
print (x > 7) # get a boolean value (i.e. True or False)
# use == to check if two values are equal
# percent is  the "modulus operator"; which is the remainder

print (math.pi)

quadratic_formula # this is called snake case -- use snake formula for Python
quadraticFormula # this is called camel case