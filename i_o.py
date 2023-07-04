print("Welcome! ")

def paye(name,sal):
    rate = 0.3
    tax = rate * sal
    net = sal - tax
    print("***********************************")
    print("Dear: ", name)
    print("Your tax payable is: ", tax)
    print("And your take-home salary is: ", net)
    print("...................................")

# The argument has to be input first.
name = raw_input("Please enter your name: ")
sal = float(input("Please input your salary here: "))

paye(name,sal)
'''
Notes:
    Python 2 has two functions 'input' and 'raw_input" to capture 
values from the keyboard, but Python 3 only has one function, 'input'.
In python 2, print was not a function, but in Python 3, it is
a function.
    In python 2, raw_input accepts everything strings but input accepts only
numerics. However, in python 3, input expects everything to
be a string.
    Type casting is converting a value from one datatype to another.
An argument can't be a string.
    Input captures values from the keyboard but everything is 
captured as a string.
    An algorithm is a step by step process of solving a problem.
    Remove dead code. (commented unnecessary code)
'''


