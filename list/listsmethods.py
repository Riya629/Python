# we learn 8 methods of list which are below:

list = [1, 4, 2, 0,1, 9]
list.append(7)
print(list)

print("\n")

list.sort()
print(list)

print("\n")

list.reverse()
print(list)

print("\n")

print(list.index(2))

print("\n")

print(list.count(1))
print("\n")

nums=list.copy() # we use copy method to copy elements in list a=we cannot copy elements using the =
print(nums)

#but in string we cannot use copy method to copy elemenst we simple use =  to copy the elements in string
nums="riya devkota"
name=nums
print(name)

list.insert(2,"Hi") # it desnot remove the elements which was previous in index 2 it shift it by replacing with hi
print(list)

nums=[400,500,600]
list.extend(nums)
print(list)
 #we can concatenate in this way too by creating an extra variable
num=list+nums
print(num)