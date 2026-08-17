# 1. __int__
class employee:
    def __init__(self,name):
        self.name=name

e=employee("sachet")
print(e.name)


#2 __str__

class employee:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name

e=employee("Riya")
print(e)


#3 __len__

class employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        return len(self.name)

e=employee("Riya")
print(len(e))


#4 __add__

class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,othernum):
        return self.num + othernum.num

a=Number(10)
b=Number(20)
print(a+b)


#5 __eq__

class Number:
    def __init__(self,num):
        self.num=num
    def __eq__(self,other):
        return self.num==other.num


a=Number(20)
b=Number(20)
print(a==b)

#6 __it__

class Number:
    def __init__(self,num):
        self.num=num

    def __lt__(self,other):
        return self.num<other.num

a=Number(10)
b=Number(20)
print(a<b)