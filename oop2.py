'''
The name of the class shouls start with a capital letter.
Things in a class are called attributes or properties. 
Below is a defined class withh attributes/properties.
'''

class Girl:
    name = "Jessica"
    age = 20
    gender = "female"
    size = "small"
    family = "kabaka"
    size_of_bra = "small"
    def greet():
        print('Hello World!')
        print('Hey World!')
        return''
    def dance():
        print("Ballet is tough!")
        return''
    def bathe():
        return'Twice a day.'
    
Girl.greet()
Girl.dance()
Girl.bathe()
print(Girl.bathe())

print(Girl.name)
print(Girl.age)
print(Girl.gender)
print(Girl.size)
print(Girl.family)
print(Girl.size_of_bra)

girl2 = Girl()

girl2.name = "Rachel"
girl2.age = 27
girl2.gender = "female"

print(f"{girl2.name} is {girl2.age} years old.")
# Literal strings (strings that represent values).

girl3 = Girl()

girl3.name = "Donna"
girl3.age = 12

print(f"{girl3.name} is {girl3.age} years old.")

'''
A method is a piece of code that defines what an object 
does to the other and itself.
And how it does it is called a behaviour. 
A method in OOP is the equivalent of a function in structured 
programming.
The lines of code within the function in structured programming 
are equivalent to behaviours in OOP.
Attributes are equivalent to variables.
All objects in the same class have the same method.
'''
