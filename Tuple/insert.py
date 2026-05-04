#We cannot directly made changes in tuple first we have to convert  it into list and operation can be perfom on it and finally converted back into tuple

countries=("Nepal", "Russia", "China", "Autralia")
fruits=("mango", "apple")
temp=list(countries) #converting the tuple into list
print(temp) #output will be in list
print(countries) #output will be in tuple

temp.append("America")
print(temp)
temp.pop(3)
print(temp)
temp.insert(3,"Australia")
print(temp)

countries= tuple(temp)
print(countries) #output will be in tuple

#conacatenating tuple by using extra variable
Tup=countries+fruits
print(Tup)

tup=(2,"apple", True)
print(tup)