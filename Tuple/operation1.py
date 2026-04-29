#slicing in Tuple
Tup=("Green", "Red", "Blue", "Orange", "Purple")
print(Tup[1:4:2])
print(Tup[:])
print(Tup[1:])
print(Tup[:5])

if "Red" in Tup:
    print("yes there is red In Tup")
else:
    print("There is no red in Tup")
    print("\n")
for i in Tup:
    print(i)
 
print("\n")

Tup=tuple(i for i in range(10)) # python dont have tuple comprehension so we have to write tupleWhy no tuple comprehension?
print(Tup)

# Python has:
# List comprehension 
# Set comprehension 
# Dictionary comprehension 
# No direct tuple comprehension 
# print(Tup)

list=(i for i in range(10))  #this generate a generator object looks like list vut use ()
print(next(list)) #produces only one output value at a time it doesnot save all list in memory