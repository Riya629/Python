#calculator using match case

num1=int(input("Enter  first number :"))
num2=int(input("Enter second number :"))
op=input("Enter operator :")
match op:
    case '+':
        result=num1+num2
        print("The sum of", num1, "+ ",num2, ":",result)
    case'-':
        result=num1-num2
        print("The subtraction of",num1, num2, ":",result)
    case'*':
        result=num1*num2
        print("The multiplication of",num1,num2, ":",result)
    case'/':
        if(num2!=0):
            result=num1/num2
            print("The division of ",num1,num2, ":",result)
        else:
            print("Cannot be zero")
    case'//':
        if(num2!=0):
            result=num1//num2
            print("The division of ",num1,num2, ":",result)
        else:
            print("cannot be zero")
    case'%':
        if(num2!=0):
            result=num1/num2
            print("The division of ",num1,num2, ":",result)
        else:
            print("cannot be zero")
    case _ :
        print("Invalid operator")
