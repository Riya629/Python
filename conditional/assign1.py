# import time
# name=input("Enter your name : ")
# recenttime=time.strftime('%H:%M:%S')
# print(recenttime)
# Recenttime=int(time.strftime('%H'))
# if(4<=Recenttime<12):
#     print("Good morning sir its", recenttime)
# elif(12<=Recenttime<17):
#     print("Good afternoon its",recenttime)
# elif(17<=Recentime<20):
#     print("Good evening sir its",recentime)
# else:
#     print("Good night sir its",recenttime)




import time
name=input("Enter your name :")
recenttime=time.strftime('%H : %M: %S %p')
Recenttime=int(time.strftime('%H'))
if(4<=Recenttime<12):
    print("Good morning",name, "it's",recenttime)
elif(12<=Recenttime<17):
    print("Good morning",name, "it's",recenttime)
elif(17<=Recentime<20):
    print("Good morning ",name, "it's",recenttime)
else:
    print("Good night ",name, "it's",recenttime)
    