# fruits=["apple","banana","orange"]
# for i,fruit in enumerate(fruits):
#     print(i,fruit)

#without enumurate function 
# nums=[2,3,4,5,5,7,8]
# i=0
# for num in nums:
#     print(num)
#     if(i==3):
#         print("Riya stop")
#     i=i+1


#with enumerate fuction         
#start=1 doesnot mean print the value strat from 1 index it mean start loop from 1 index 
nums=[2,3,4,5,5,7,8]
for i,num in enumerate(nums ,start=1):
    print(i,num)
    if(i==3):
        print("Riya stop")
        i=i+1
