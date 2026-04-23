# num1=0
# num2=1

# n=int(input("Enter the number of series: "))
# print("The fibonnaci series are: ")
# for i in range(1,n+1):
#    print(num1,end= " ")
#    num3=num1+num2
#    num1=num2
#    num2=num3

#fibonacci using while loop

num1=0
num2=1
n=int(input("Enter the number of series in fibonnaci series"))
print("The fibonacci series are: ")
i =0
while(i<=n):
    print(num1, end=" ")
    num3=num1+num2
    num1=num2
    num2=num3
    i=i+1