#program to find factorial of a number
def factorial(num):
    if(num==0 or num==1): #Inpython we use or instead of ||
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter a number: "))
print(factorial(num))




#Fibonnaci Program using recursion

def fibo(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

num=int(input("Enter the number of series: "))
print("fibonacci series :")
for i in range(num):
    print(fibo(i), end=" ")