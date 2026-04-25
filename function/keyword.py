#This are the example of keyword argument

def name(Fname, Mname, Lname):
    print(Fname,Mname,Lname)

name(Mname="prasad",Fname="Riyan",Lname="Devkota") #Lname should also be written

print("\n")
#sum of numbers (tuple)
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)
average(5,4,3,2)


print("\n")

def average(num1):
    return num1/2
sum=average(12)
print(sum)
print(average(12)) #we can do in this way too