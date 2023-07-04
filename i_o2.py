print("Welcome! ")

def paye(name,sal):
    rate = 0.3
    if sal >= 300000:  
        tax = rate * sal
        net = sal - tax
        print("***********************************")
        print("Dear: ", name)
        print("Your tax payable is: ", tax)
        print("And your take-home salary is: ", net)
        print("...................................")
    else:
        print("Dear: ", name)
        print("Your salary is non-taxable.")

name = raw_input("Please enter your name: ")
age = raw_input("Please enter your age: ")
location = raw_input("Please enter your location: ")
job = raw_input("Please enter your occupation: ")
sal = float(input("Please input your salary here: "))

print(age,location,job)

paye(name,sal)

# Rename assignment file as 'GraciaAtiku.py' and upload on Google classroom.

'''
Next, modify this code to capture someone's location, 
age, and occupation, date of birth by 6pm. Submission 
mode to be disclosed before 6pm through WhatsApp.
'''