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

print("Welcome to Auntie Esther's Nursery School!")
print("Please input the following details as instructed below.")
name = input("Name of child: ")
clas = input("Class of child: ")
date = input("Date of birth: ")
guardian = input("Next of kin: ")
location = input("Area of residence: ")
print("The school fees full amount is Ugx.300,000 per child per term.")
pay = input("Is the school fees balance cleared?(Yes/No): ")

def summary(name,clas,date,guardian, location,pay):
    if pay == "Yes":
        print("Fees have been fully paid.")
    else:
        print("Please pay the full amount by 18th July, 2023.")
    print("Thank you!")
summary(name,clas,date,guardian,location,pay)

student = {
    "Name of Child": name,
    "Class of Child": clas,
    "Date of Birth": date,
    "Next of Kin": guardian,
    "Area of Residence": location,
    "School fees": pay
}

students = []
students.append(student)
print(students)
for child in students:
    print(child)
