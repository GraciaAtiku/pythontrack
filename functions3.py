def add(num1,num2):
    num3 = num1 + num2
    print (num3)

def sub(num1,num2):
    num3 = num1 - num2
    print (num3)

# Forcing the functions to communicate.

'''
The Python return statement is a special statement that 
you can use inside a function or method to send the function's 
result back to the caller.
'''

def add2(num1,num2):# num1 & num2 are called parameters.
    num3 = num1 + num2
    return num3# Where there's a return statement, the lines below can't be executed.

def sub2(num1):
    num3 = add2(7,10) - num1
    print (num3)

sub2(5)# 5 is an argument or actual parameter or formal parameter.

'''
The above functions are called dynamic functions or parameterized 
functions.
When you print a function call without a return statement 
and then you run, you will get a value, 'none'.
A function that calls a returned value from another function is called 
a calling function.
'''
add2(2,3)

ans = add2(30,50)
print (ans)
print (add2(2,3))