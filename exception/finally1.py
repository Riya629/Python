def func1():
    try:
        list=[2,3,4,5]
        l=int(input("Enter a number:"))
        print(list[l])
        return 1
    except IndexError:
        print("some error occured")
        return 0
    finally:
        print("Iam always executed")

x=func1()
print(x)

# Here if finally is ot used than the print t statement will not be executed beacuse teh return means function finised exit immediately andgo back 
#return 1 means sucessfully completed and function finished
#return 0 means failure and function stops and below that nothing is orinted but
#it finally is used thatcit is printed no matter if exception occur or not finally block is always executed