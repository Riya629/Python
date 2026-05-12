#we can use multiple except to handle exception
try:
    num=int(input("Enter a number"))
    a=[2,3]
    print(a[num])
except ValueError:
    print("value entered is not integer")
except IndexError:
    print("Index error")
except Exception as e:
    print(e)


