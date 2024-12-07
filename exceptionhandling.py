try:
    print(number)

except:
    print("An error has occurred")


num1 = 39
num2 = 3

try:
    print(num1 / num2)
except:
    print("ZeroDivisionError has occurred")

finally:
    print("Success")

#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.