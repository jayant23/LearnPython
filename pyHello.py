names = ["Jayant","Mudit","Anmol","Param"]
print(names[1:2])

def func(a):
    if a == 0:
        print(False)
    else:
        print(True)

func(0)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for column in matrix:
    print(column[1])

numbers = [4,5,1,2,9,7,6,8,5]
numbers = 10
print(numbers)

customer = {
    "name":"jayant",
    "age":30,
    "is_verified":True
}
print(customer.get("birthdate","jan 1 1990"))
message = 'input(">")'
word = message.split(' ')
emojis = {
    ":)":"😊",
    ":(":"😚"
}
output = ""
for w in word:
    output += emojis.get(w,w) + " "
print(output)

def great_user(name):
    print(f'Hi {name}')
    print('welcome aboard')

print('start')
great_user("jayant")
print('finished')

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def move(self):
        print('move')

    def draw(self):
        print('draw')

point = point(10,20) 
print(point.x)

class person:
    def __init__(self, name):
        self.name=name
        self.talk()

    def talk(self):
        print('i am '+self.name)

    def __str__(self):
        return f'This is person object {self.name}'

jayant = person("jayant")
jayant.talk()
print(jayant)   

class Mammal:
    def walk(self):
        print('walk')
    
    def __init__(self,legs):
        self.legs = legs


class Dog(Mammal):
    def bark(self):
        print('bark', self.legs)

class Cat(Mammal):
    def be_annoying(self):
        print('annoying', self.legs)

cat1 = Cat(4)
cat1.be_annoying()


dog1 = Dog(3)
dog1.bark()
dog1.walk()    

import converters
from converters import kg_to_lbs

kg_to_lbs(100)

print("kg to lbs ",converters.kg_to_lbs(70))


class Person:
    def __init__(self,name,lname):
        self.name=name
        self.lname = lname   
    def talk(self):
        print(f'Hi, im {self.name, self.lname}')


john = Person("jayant","kumar")
john.talk()


# Inheritance

class persons(object):
    # Constructor
    def __init__(self,name):
        self.name=name
    

    # to get name
    def getName(self):
        return self.name
    

    # To check if the person is employee
    def isEmployee(self):
        return False    
# Inherited or Sub class (Note Person in bracket)
class Employee(persons):

    def isEmployee(self):
        return True        # here we return true
    # Driver code
    emp = persons("Greek1")
    print(emp.getName(),emp.isEmployee())

class Base1(object):
        def __init__(self):
            self.str1 = "Geek1"
            print ("Base1" )        
  
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"        
        print ("Base2" )           
  
class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print ("Derived" )     
          
    def printStrs(self):
        print(self.str1, self.str2) 

ob = Derived() 
ob.printStrs()         