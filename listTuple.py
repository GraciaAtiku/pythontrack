# List, tuple and dict(dictionary) in detail.
# Labels(positions) start with 0.(indices)
# Python gives us the allowance to move backwards. In this case, we start with -1.
my_list = [0,1,2,3,4,5,6,7,8,9]
print (my_list[5])
my_list2 = [0,10,20,30,40,50]
print (my_list2[5])
print (my_list2[-1])

osman = [100,[200]]
print (osman[1][0])
osman2 = [1000,[[2000,3000]]]
print (osman2[1][0][1])

# A list is a mutable datatype. Once a list is created, it can be appended(values can be added) and popped (last value is removed).
# Example of a mutable list.
osman.append (1000)
print (osman)
osman.pop ()
print (osman)
fruits = ['orange','pineapple']
fruits.append ('apple')
print (fruits)
fruits.pop ()
print (fruits)

# Tuples in detail.
# We use indices again.
# A tuple is an immutable datatype. One can only access values in a tuple but cannot add or remove any values.
my_tuple = (10,20,30,40,50)
print (my_tuple)

# Dict (dictionary) in detail.
# A dictionary is identified by braces. They are also mutable like lists.
zebra = {'name':'Tongs', 'legs':4, 'color':'black & white', 'sex':'male'}
print (zebra.keys())
print (zebra)
zebra.__delitem__ ('name')
print (zebra)

'''
Note: Types of comments.
Multi-line comments are written above every function. 
Single-line comments can be written inside the function.
'''

# Assigmnent: Group statements and define functions.

'''
multi-line comment
'''
def my_lists():
    # single line comment
    my_list = [0,1,2,3,4,5,6,7,8,9]
    print (my_list[5])
    my_list2 = [0,10,20,30,40,50]
    print (my_list2[5])
    print (my_list2[-1])

my_lists()

'''
multi-line comment
'''
def osmans():
    osman = [100,[200]]
    print (osman[1][0])
    osman2 = [1000,[[2000,3000]]]
    print (osman2[1][0][1])
    osman.append (1000)
    print (osman)
    osman.pop ()
    print (osman)

osmans()

'''
multi-line comment
'''
def basket():
    fruits = ['orange','pineapple']
    fruits.append ('apple')
    print (fruits)
    fruits.pop ()
    print (fruits)

basket()

'''
multi-line comment
'''
def mapping():
    zebra = {'name':'Tongs', 'legs':4, 'color':'black & white', 'sex':'male'}
    print (zebra.keys())
    print (zebra)
    zebra.__delitem__ ('name')
    print (zebra)

mapping()