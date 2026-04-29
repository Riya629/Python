tup = (1, 2, 3, 4, 5)
print(type(tup))

print("\n")
if 2 in tup:
    print("yes 2 is in tup")
else:
    print("2 is not in tup")

print(tup[0])
print(tup[1])
print(tup[2])
print("\n")
print(len(tup))
print(tup[-2])  # negavite and positive slicing is same as list in tuple
# But in this case if only one  integer element is without common python will give it datatype int so we must use comma , for single element in tuple
tup = 1
print(type(tup))

# tuple is immutable we cannot change tuple

# tup=(111,222,333,444)
# tup[0]=1
# print(tup) #This will generate error cause we cannot change the tuple it is immutable

list = [11, 22, 33, 44]
list[0] = 2
print(list)  # but we can chnage list so it is correct
