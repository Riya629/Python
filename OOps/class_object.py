#Introducing to class and object
class Student:
    name="Riya"
    age=20
s=Student()     #creates and objects s is reference that points to object and object are somewhere in memory
print(s.name)
print(s.age)


#using method
# class student2:
#     def info(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name)
#         print(self.age)
# s2=student2()
# s2.info("Sachet",25)

#or
class Student2:
    def info(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
s2=Student2()
s3=Student2()
s2.info("Riya",23)
s3.info("saciya",24)
s2.display()
s3.display()