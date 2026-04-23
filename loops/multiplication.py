# num=int(input("Enter the number for multiplication :"))
# print("The multiplication of", num ,"is :")
# for i in range(1,11):
#     multi=num*i
#     print(num, "*", i, " =", multi)
   

#Multiplication table using while loop

num=int(input("Enter  the number for multiplication: "))
i=1
print("The multiplication of entered number is: ")
while(i<=10):
    multi=num*i
    print(num, "*", i, " =", multi)
    i=i+1