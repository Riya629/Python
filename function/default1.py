# we can pass default value in this way too
def average(num1=2, num2=4):
    print((num1 + num2) / 2)


average()

print("\n")


# we can give default value in this way too
def average():
    num1 = 2
    num2 = 3
    print((num1 + num2) / 2)


average()

print("'\n")


# This this case we already pass argument and also pass value in function call but it give more prioriy to the functionn class pass value
#default value is overridden
def average(num1=4, num2=2):
    result = (num1 + num2) / 2
    print(result)


average(2, 2)
print("\n")

#Here default argument and value is passed during the function call then if no argument is passed the default value is used bt the python
def average(num1=2, num2=2):
    print((num1 + num2) / 2)


average(2)

#Another example of default argument
def name(fname, Mname="prasad", Lname="Devkota"):
    print(fname,Mname,Lname)
name("Riyan",)