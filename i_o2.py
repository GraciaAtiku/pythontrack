print("Welcome! ")

def paye(name,sal):
    rate = 0.3
    if sal >= 300000:  
        tax = rate * sal
        net = sal - tax
        print("***********************************")
        print("Dear ", name)
        print("A ", age, "year old")
        print("A ", job)
        print("In ", location)
        print("Your tax payable is ", tax)
        print("And your take-home salary is ", net)
        print("...................................")
    else:
        print("***********************************")
        print("Dear ", name)
        print("A ", age, "year old")
        print(job)
        print("In ", location)
        print("Your salary is non-taxable.")
        print("...................................")
    print('Thank you!')

name = input("Please enter your name: ")
age = input("Please enter your age: ")
location = input("Please enter your location: ")
job = input("Please enter your occupation: ")
sal = int(input("Please input your salary here: "))

paye(name,sal)

'''
Assignment: Modify this code to capture someone's location, 
age, and occupation.
'''
