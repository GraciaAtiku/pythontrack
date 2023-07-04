# Operators in Python.
# What are operators?
# Operators tell the computer what to do with an operand.
# What is an operand?
# An operand is what an operator acts upon.

# Different categories of python operators and their meaning.
# 1) Arithmetic operators.(+,-,*,/,//,%,**)
# Examples
num1 = 10
num2 = 20
# addition symbol
print (num1 + num2)
# subtraction symbol
print (num1 - num2)
# multiplication symbol
print (num1 * num2)
# division symbol
print (num1 / num2)
# floor division symbol
print (num1 // num2)
# modulus symbol 
print (num1 % num2)
# exponentiation symbol 
print (num1 ** num2)

# 2) Assignment operators.(=,+=,-=,*=,/=,%=,**=)
# = means 'assigned to'
num3 = 50
num4 = 100
num3 += num4 #(This is the same as num3 is assigned to num3 + num4.)
print (num3)
num3 -= num4 #(num3 = 150 now)
print (num3)
num3 /= num4 #(num3 = 50 now)
print (num3)
num3 *= num4 #(num3 = 0 now)
print (num3)

# 3) Comparison operators.(==,!=,>,<,>=,<=)
print (num1 == num2)
print (num1 != num2)
print (num1 > num2)
print (num1 < num2)
print (num1 >= num2)
print (num1 <= num2)

# 4) Logical operators.(and,or,not)
print (True and True)
print (True and False)
print (True or False)
print (not True)

# 5) Identity operators.(is,is not)
print (num3 is num4)
print (num3 is not num4)

# 6) Membership operators.(in, not in)
name = 'Gracia'
print ('a' in name)
print ('o' in name)
print ('A' in name)
print ('o' not in name)