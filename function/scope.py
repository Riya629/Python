x=4 #global variable
def my_function():
    x=2
    y=5
    print(y)
    print(x) #local variable
my_function()
print(x) #print x=4


#butif you want ot modify your variable type local variable to global variable

x=2
def func():
    global x
    x=4 # it become global variable
    y=2
    print(x)
    print(y)
func()
print(x) #line by line execution soo x=4 is printed