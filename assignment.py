'''
Assignment: Imagine Auntie Esther Nursery School is looking for 
a program to record new students of nursery class. Create an interactive
program with atleast one function. Capture from the student. Full name.
Date/Year of birth. Guardians name. Class. Location. State of payment
(Yes/No). It should give out the summary of the registered student and 
give out the amount of money they should pay. The captured values should 
be appended in a list called 'students'.
Push to the repository for the class to be created by Trinity.
By Friday before class. Also post yesterday's assignment there.
'''

def exmp():
    my_list = []
    num = int(input("Please enter your lucky number: "))
    my_list.append (num)
    print(my_list)
    for item in my_list:
        print(item)

#exmp()
# A loop can be created instead.

print("Welcome!")
print("Please input the student details as instructed below:")
name = raw_input("Name of student: ")
clas = raw_input("Class of student: ")
date = raw_input("Date of birth: ")
guardian = raw_input("Next of kin: ")
location = raw_input("Area of residence: ")
pay = raw_input("State of payment: ")

def summary():
    print(name, clas, date, guardian, location, pay)
    if pay == "yes":
        print("Thank you!")
    else:
        print("Please pay the full amount by 18th July, 2023.")

summary()
