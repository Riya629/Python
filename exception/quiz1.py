
try:
    str=input("Enter a string :")
    if(str!="quit"):
     raise ValueError("The string you entered is not correct")
    else:
        print("The string you eneterd matched the str")
except ValueError as e:
     print(e)

