# Functions
# A function is a named group of statements that is performing a specific task.
num1 = 50
num2 = 100
num3 = num1 + num2
print (num3)
# def means defining the function as shown below. It has to be called to action/for execution as in line 12.
def sum():
    num1, num2 = 30, 45
    num3 = num1 + num2
    print (num3)
sum()

def sub():
    num1, num2 = 70, 25
    num3 = num1 - num2
    print (num3)
sub()

def rem():
    num1, num2 = 30, 7
    num3 = num1 % num2
    print (num3)
rem()

def my_list():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    print (list1[3])
my_list()

# The above are called static functions.