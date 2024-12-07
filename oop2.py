class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def movement(self):
        print("Person is walking")


a = Person("George",19,"Male")
print(a.name)
print(a.age)

b = Person("Esther",23,"Female")
print(b.name)
print(b.age)

c = Person("William",34,"Male")
print(c.name)
print(c.age)



