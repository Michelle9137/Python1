#Built-in Library functions
y = max(56,90,23,14,78)
print(y)


x = min(23,45,67,32,89)
print("The minimum value is ", x)

z = pow(2,3)
print(z)

#User-defined functions
def greeting():
    print("Hello there")
greeting() #Calling a function


def multiply():
    num1 = 23
    num2 = 10
    print(num1*num2)

multiply()

#Parameter/ Variable and Arguments/Values
def add(a,b):
    print(a+b)

add(3,4)
add(45,60)


def employee(fullname,age,position,status):
    print(fullname,age,position,status)

employee("Michelle John",21,"Manager","Single")
employee("Kelvin Jones",23,"Secretary","Married")
employee("Jay Ben",31,"HR","Married")
