'''
Personal assignment: Read about the while loop in python.
Get examples to demonstrate what you have understood.
'''

'''
Python While Loops
    With a while loop, we can execute a set of statements as 
long as a condition is true.
'''
def example1():
    num1 = 1
    while num1 <= 10:
        print (num1)
        # We increment num1 or else the loop will be endless.
        num1 += 1

example1()

'''
The break statement.
    With the break statement we can stop the loop even
if the while condition is true.
'''
def example2():
    num1 = 1
    while num1 <= 10:
        print(num1)
        if num1 == 7:
            break
        num1 =+ 1

example2()

'''
The continue statement.
    With the continue statement we can stop the current 
iteration, and continue with the next. (skip the value)
'''
def example3():
    num1 = 1
    while num1 <= 10:
        num1 += 1
        if num1 == 3:
            # It skips 3 and continues to 11.
            continue
        print(num1)

example3()

'''
The else statement.
    With the else statement we can run a block of code once 
the condition no longer is true.
'''
def example4():
    num1 = 1
    while num1 <=10:
        print(num1)
        num1 += 1
    else:
        print("num1 is no longer less than or equal to 10")

example4()

# Source:https://www.w3schools.com/python/python_while_loops.asp

# A different example.
# The loop will run only once.
def example5():
    thirsty = True
    while thirsty:
        print("Have a glass of water.")
        # The statement below prevents the endless loop.
        thirsty = False

#example5()

# Source:https://www.codecademy.com/resources/docs/python/loops

'''
Assignment: Define two functions that can output even and odd numbers
in a range of 100 in tens. (e.g, 10,20,30)
Submission: Send through email.
'''
'''
This pair of functions is of a smaller range of 10.
'''
def even():
    num1 = 0
    while num1 <= 10:
        print(num1)
        # A repeated increment of 2 on 0 ensures even number output.
        num1 += 2

#even()

def odd():
    num1 = 1
    while num1 <= 10:
        print(num1)
        # A repeated increment of 2 on 1 ensures odd number output.
        num1 += 2

#odd()

'''
This other pair of functions is of range of 100 in tens.
'''
def even():
    num1 = 10
    while num1 <= 100:
        print(num1)
        # A repeated increment of 10 on 10 ensures even number output.
        num1 += 10

#even()

def odd():
    num1 = 5
    while num1 <= 100:
        print(num1)
        # A repeated increment of 10 on 5 ensures odd number output.
        num1 += 10

#odd()