#Assignment from list and list comprehension

#1 print from 1 to 10 using loop
list=[]
for i in range(0,11):
    list.append(i)
print(list)

print("\n")

#2 Store item using append
fruit=[]
fruit.append("apple")
fruit.append("mango")
fruit.append("banana")
print(fruit)
print("\n")

 #3 print all elemnts using loop
nums=[5,10,15,20,25]
for i in nums:
    print(i)
print("\n")

#create a new list by adding 1 to each element using a loop
nums=[2,4,6,8,10]
new_list=[]
for i in nums:
    new_list.append(i+1)
print(new_list)
print("\n")
#list comprehension
nums=[i for i in range(1,11)]
print(nums)

print("\n")

#printing even numbers from 2 to 20
nums=[i for i in range(2,21) if i%2==0]
print(nums)

print("\n")
# priting square of numbers from 1 to 7
square=[i*i for i in range(1,8)]
print(square)

print("\n")

#printing only odd numbers from the list
nums = [1,2,3,4,5,6,7,8,9]
for i in nums:
    if i%2!=0:
        print(i)

print("\n")
# with list comprehension
nums = [1,2,3,4,5,6,7,8,9]
odd=[i for i in nums if(i%2!=0)]
print(odd)

print("\n")

#printing which is divisible by 3
nums = [3,6,9,12,15]
div=[i for i in nums if(i%3==0)]
print(nums)