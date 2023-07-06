print("Welcome! ")

def paye(name,sal):
    rate = 0.3
    if sal >= 300000:  
        tax = rate * sal
        net = sal - tax
        print("***********************************")
        print("Dear ", name)
        print("A ", job)
        print("In ", location)
        print(age, "years of age.")
        print("Your tax payable is ", tax)
        print("And your take-home salary is ", net)
        print("...................................")
    else:
        print("***********************************")
        print("Dear: ", name)
        print("A ", job)
        print("In ", location)
        print(age, "years of age.")
        print("Your salary is non-taxable.")
        print("...................................")
    print('Thank you!')

name = raw_input("Please enter your name: ")
age = raw_input("Please enter your age: ")
location = raw_input("Please enter your location: ")
job = raw_input("Please enter your occupation: ")
sal = input("Please input your salary here: ")

paye(name,sal)

'''
Assignment: Modify this code to capture someone's location, 
age, and occupation, date of birth.
'''
