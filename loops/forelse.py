for i in range(5):
    if(i==3):
        break
    print(i)
else: #else part is printed when our loop completed noramlly but with break if it is terminated it will not be printed
    print("else part is printed") #since the loop doesnot finish iteration normally the python says nope we wont run the else


i=0
while(i<5):
    if(i==3):
        break #same here in while loop too the loop ended beacuse of break not normally so else aort is not printed
        print(i)
        i=i+1
else:
     print("loop ended")
