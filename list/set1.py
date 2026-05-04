riya = { 1,2, 3, 4, 2,}  # this will print datatype dic beacuse both the set and dictioanry are written using{}
print(type(riya))
print(riya)  # output will be in same order means same like inout with bracket but using loop individually printed
for i in riya:
    print(i)
# but to print set datatype

riya = set()  # if it is empty then only peint set class ortherwise it will show error
print(type(riya))

#union
country1={"nepal","india","china"}
country2={"america","australia","canada"}
country1.union(country2) #it does not chnage the original set
print(country1) # only print cities 1 no concatetation
country3=country1.union(country2) #it only chnages the original set
print(country3) 

#update() if chnages the orignal set

cities1={"bharaptur","magalpur","jagatpur"}
cities2={"gitanagar","pateni","sitalpani"}
cities1.update(cities2) #it changes the original set
print(cities1) #combine all cities1 and cities2 together


#intersection and intersection_update
fruits={"mango","apple","banana"}
fruits2={"orange","watermelon","lemon","apple"}
fruits.intersection(fruits2) #this doesnot change or update anything so it deosnot update on original set
print(fruits)
#we should do
fruits3=fruits.intersection(fruits2) #This provide the common element
print(fruits3)


#intersection_update
#This make change update on original set
fruit={"mango","banana","litchi"}
fruits2={"mango","litchi","peach"}
fruit.intersection_update(fruits2)
print(fruit)
print("\n")

#symmetric_difference   produce the value which is not in common from both
fruit={"mango","banana","litchi"}
fruits2={"mango","litchi","peach"}
fruit3=fruit.symmetric_difference(fruits2)
print(fruit3)

#symmetric_difference_update()
fruit={"mango","banana","litchi"}
fruits2={"mango","litchi","peach"}
fruit.symmetric_difference_update(fruits2)
print(fruit)
print("\n")

#difference (it output the value which is only present in one set fruit as it is compare with fruits2)
fruit={"mango","banana","litchi"}
fruits2={"mango","litchi","peach"}
fruit3=fruit.difference(fruits2)
print(fruit3)
 
print("\n")

#isdisjoint()
fruit={"mango","banana","litchi"}
fruits2={"mango","litchi","peach"}
print(fruit.isdisjoint(fruits2))
print("\n")

fruit={"mango","banana","litchi"}
fruits2={"orange","peach","avocado"}
print(fruit.isdisjoint(fruits2))

print("\n")

#issuperset() (check whether the item present in subset are present in original set or not)
#check deos oxfrod contain all item which are presnt in oxford2
oxford={"Riya","sandhikshya","sachet"}
oxford2={"Riyan", "Riya","pabitra"}
print(oxford.issuperset(oxford2))

oxford={"Riya","sandhikshya","sachet","Riyan", "Riya","pabitra"}
oxford2={"Riyan", "Riya","pabitra"}
print(oxford.issuperset(oxford2))


#isubset (opposite of issuperset check whether the item present in original set are vaibale in subset or not )
#check whether oxford contain all item presnt in oxford or not


oxford={"Riya","sandhikshya","sachet","Riyan", "Riya","pabitra"}
oxford2={"Riyan", "Riya","pabitra"}
print(oxford.issubset(oxford2))


oxford={"Riya","sandhikshya","sachet","Riyan", "Riya","pabitra"}
oxford2={"Riya","sandhikshya","sachet","Riyan", "Riya","pabitra"}
print(oxford2.issubset(oxford))

#some methods
#add() it is used to ass a single elements
fruits={"orange",",mango","apple"}
fruits.add("banana")
print(fruits)

#update() its is used to insert a large elements
fruits={"orange",",mango","apple"}
fruits2={"peach","avocado","litchi"}
fruits.update(fruits2)
print(fruits)

#remove() it is used to remove elemnys from the set we can use remove to show error message
fruits={"orange","mango","apple"}
fruits.remove("mango")
print(fruits)

#discard  same as remove but doesnot generate error message
fruits={"orange","mango","apple"}
fruits.discard("mango")
print(fruits)

#pop() it is used to remove the last elemnts from the set
fruits={"orange","mango","apple"}
fruits.pop()
print(fruits)

#del it is not a method buta keyword to delete the set
# fruits={"orange","mango","apple"}
# del fruits
# print(fruits) #already deleted set so trying to print it generate error

# # clear() it is used to clear the set

# fruits={"orange","mango","apple"}
# fruits.clear()
# print(fruits)


#checking the items in set

info={"Riya",20,"bharatpur"}
if 20 in info:
    print("yes its is")
else:
    print("no it's not")