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
message = input(">")
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
    def talk(self):
        print('m nhi khelta')

jayant = person()
jayant.talk()        