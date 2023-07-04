'''
A loop is a mechanism or statement that helps us to
ask the computer to perform tasks repeatedly.
We use a for loop.
Item (any variable name) represents a value at a 
particular point of the range.
10 means count 10 times
'''

def my_count():
    for item in range (10):# a for loop
        print (item)

my_count()
'''
Trying to access list elements using a loop.
'''
def example2():
    languages = ['python', 'javascript', 'java', 'c', 'c++']
    for language in languages:
        print (language)

example2 ()

def example3(num1):
    for number in range (num1):
        print (number)

example3 (7)
example3 (13)

def my_lang():
    languages = ['python', 'javascript', 'java', 'c', 'c++']
    for language in languages:
        if language == 'python':
            print ('You are currently in Python class.')

my_lang ()

def even(num):
    for number in range (num):
        if number % 2 == 0:
            print (number)

even(5)

# Alter even function, call it odd, and it should be printing out odd numbers.
# Write an email. Post the function in the body of the email.

def odd(num):
    for number in range (num):
        if number % 2 != 0:
            print (number)

odd(5)

def power(p):
    my_po = p**2
    if my_po % 2 == 0:
        print ("The power is an even number.")
    else:
        print ("The power is an odd number.")

power(7)