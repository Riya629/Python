#accessing the dictinoary

dict={'name':'Riya','age':20, 'eligible':True}
print(dict)

#accessing the individual key
dict={'name':'Riya','age':20, 'eligible':True}
print(dict['name'])
#or
print(dict.get('name'))

#Accessing all key
dict={'name':'Riya','age':20, 'eligible':True}
print(dict.keys())

#Acessing all value

dict={'name':'Riya','age':20, 'eligible':True}
print(dict.values())

#Acesssing all keys and values
dict={'name':'Riya','age':20, 'eligible':True}
for i in dict:
    print(i) #in this way only the keys are printed

    #acessing the key value pair
dict={'name':'Riya','age':20, 'eligible':True}
print(dict.items())
for key in dict.keys():
    print(f"{key} {dict[key]}")
















detail={'name':'Riya','age':20, 'email':'riyadevkota2062@gmail.com','gender':'female'}
print(detail) #accessing the dictinaory
print(detail.keys())
print(detail.values())
print(detail.items())
print(detail['name']) #acessing the single value
print(detail.get('name'))
for key in detail.keys():
    print(f"{key}:{detail[key]}")