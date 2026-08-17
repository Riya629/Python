list=[2,3,4,"harry",True]
if 2 in list:
    print("yes")
else:
    print("no")


colors=["Red", "Green", "blue", "Orange"]
print(colors[1])
print(colors)
print(colors[:]) # we can print list in this way too
print(colors[1:])
print(colors[:3])
print(len(colors))
print(colors[-2]) 

#without list comprehension
numbers = []
for i in range(5):
    if(i%2==0):
     numbers.append(i)

print(numbers)

#with list comprehension
list=[i for  i in range(10) if(i%2==0)]
print(list)


list=[i*i for i in range(10) if i%2==0]
print(list)

amount=int(input("Enter salary:"))
if amount<999:
    vat_amt=amount*13/100
    discount=0
elif amount<9999:
    vat_amt=vat_amt+amount-999*13/100
    discount=vat_amt*5/100




even=[i for i in range(10) if(i%2==0)]
# print(even) givr answer in from of list
for i in even:
    print(i)