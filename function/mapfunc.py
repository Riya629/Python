# #exmaple of map
# num=[1,2,3,4]
# def func(x):
#     return x*x
# num2=map(func,num)
# print(list(num2))
# # print(num2)  map doesnot store in normal list

# #Example of filter

# num=[1,2,3,4,5,6]
# def even(x):
#     return x%2==0
# result=filter(even,num)
# print(list(result))

# #using lambda function

# num=[6,7,8,9,2]
# even=filter(lambda x:x%2==0,num)
# print(list(even))


# #reduce function

from functools import reduce
l=[1,2,3,4,5]
def sum(x,y):
    return x+y
li=reduce(sum,l)
print(li)

#using lambda funcrion

num=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,num)
print(sum)