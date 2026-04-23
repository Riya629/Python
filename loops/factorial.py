#Factorial program using for loop
num=int(input("Enter a number :"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


#Factorail program using while loop
i=1
fact=1
n=int(input("Enter a  number  : "))
while(i<=n):
    fact=fact*i
    i=i+1
print(fact)