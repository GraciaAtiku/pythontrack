'''
Below is a dynamic function defined as 'tests', with two parameters, 
'test1' and 'test2'. 
'''

def tests(test1, test2):
	# Parameters test1 and test2 are compared.
	if test1 == test2:
		# If test1 is equal to test2, the value of test1 is returned.
		return test1
	else:
		# If test1 is not equal to test2, the value of test2 is returned.
		return test2
'''
The string 'Please enter Marks for test one: ' is shown in the terminal using 
the 'input' function. The value typed in the terminal is assigned to the variable 
'test1' and changed to an integer by the 'int' function.
'''
test1 = int(input('Please enter Marks for test one: '))
'''
The string 'Please enter Marks for test two: ' is shown in the terminal using 
the 'input' function. The value typed in the terminal is assigned to the variable 
'test2' and changed to an integer by the 'int' function.
'''
test2 = int(input('Please enter Marks for test two: '))

'''
Below is a dynamic function defined as 'courseWrk', with one parameter, 
'cswork'. 
'''
def courseWrk(cswork):
	# The value of tests(test1,test2) function is assigned to testsMark.
	testsMark = tests(test1,test2)
	# The value of (cswork + testsMark)/2 is assigned to avgtestsCswork.
	avgtestsCswork = (cswork + testsMark)/2
	# The value of (avgtestsCswork * (40/100)) is assigned to fnltestsCswork.
	fnltestsCswork = avgtestsCswork * (40/100)
	# The string with multiple dots should be printed.
	print('..............................')
	# The string 'your final coursework marks is: ' and the value of fnltestsCswork should be printed.
	print('your final coursework marks is: ', fnltestsCswork)
	# The string with multiple dots should be printed.
	print('..............................')
'''
The string 'Please enter your course work Marks: ' is shown in the terminal using 
the 'input' function. The value typed in the terminal is assigned to the variable 
'cswork' and changed to an integer by the 'int' function.
'''
cswork = int(input('Please enter your course work Marks: '))
# The 'courseWrk' function is called to execute the code with an argument of the value of 'cswork'.
courseWrk(cswork)

'''
The code above allows someone to enter in the marks for test one, test two, and course work.
The average of test two and course work marks are calculated and multiplied by '40/100'. The 
result which is the final coursework marks are printed for them to see.
'''