age=int(input("Enter your age :"))
mark=int(input("Enter your marks :"))
if(age>18):
    if(mark>45):
        print("your are eligible")
    else:
        print("you are not eligible due to marks")
else:
    print("you are not  elibile due to age")