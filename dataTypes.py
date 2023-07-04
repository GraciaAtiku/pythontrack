# Data Types
# Data types refers to categorization of data values/operands that are going to be stored in the variable.
# Any character or number put in quotation changes its data type.
# Examples of data types include; Numeric, String, Sequence, Mapping, Boolean, Set.

# 1) Numerics.(int,float,complex)
# Integer values are numeric whole numbers.
# Any value with a decimal point is a float.
num1 = 1000
num2 = 1000.0
num3 = 1 + 5j
print (type (num1))
print (type (num2))
print (type (num3))

# 2) String.(str)
# Any value in '' or "" is called a string.
num4 = '1000'
print (type (num4))
name = 'Gracia'
print (type (name))

# 3) Sequence.(list,tuple,range)
# A list is a collection of values in [].
# parentheses (), square brakets [], braces {}
my_list = [0,2,4,6]
print (type (my_list))
my_list2 = [0,2,4,6,'Gracia',10.5]
print (type (my_list2))
my_tuple = (0,2,4,6)
print (type (my_tuple))

# 4) Mapping.(dict)
my_dict = {'Uganda' : 'Kampala', 'Italy' : 'Rome', 'France' : 'Paris', 'Tanzania' : 'Dodoma'}
print (type (my_dict))

# 5) Boolean.(True or False)

# 6) Sets
# A set is a data type that represents an unordered list.
# A set eliminates repeated values.
my_set = {0,5,10,15,20}
print (my_set)
my_set2 = {5,5,10,10,15,20,20}
print (my_set2)
print (set(my_dict))