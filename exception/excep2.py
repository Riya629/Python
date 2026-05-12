#taking input and printing reciprocal and handling if divided by zero
try:
    num=int(input("Enter a number: "))
    res=1/num
    print(res)
except ZeroDivisionError:
    print("divide by zero")

#Write a program that:
# takes input from user converts it to integer prints "Valid Number"handles ValueError

try:
    num=int(input("Enter a number:"))
    print("valid number")
except ValueError:
    print("please enter a valid integer")

