class AgeError(Exception): #create the custom error type a meaningful error can be created
    pass
try:
    age=int(input("Enter your age :"))
    if(age<18):
        raise AgeError("you are not eligible to vote")
    else:
        print("you are eligible to vote")
except AgeError as e:
    print(e)

#without using creating a class we can still handle the error and create and throw error but it will be same for different types of error like value error
#but if we derived the builtin exception and create a new and meaningfull type of exception than it will be easy to know exaclty the type of error