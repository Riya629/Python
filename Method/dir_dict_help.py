class student:
    "hi iam riya"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        """so this is doctring"""
        print(self.name)
        print(self.age)
s=student("Riya",20)
print(dir(s)) #return the list of attribute and methods of object
print(dir(student)) #return the list of attribute and methods of class
print(s.__dict__) #return the atrribute and value of the object
print(student.__dict__)


help(student)
print(s.display.__doc__)