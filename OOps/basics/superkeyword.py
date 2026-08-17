# #methods exmaple
# class parentclass:
#     def parent_method(self):
#         print("Parent class methods")

# class childclass(parentclass):
#     def child_class(self):
#         print("child class method")
#         super().parent_method()
#     def parent_method(self):
#         print("parent method of child class")
#         super().parent_method()
# c=childclass()
# c.child_class()
# c.parent_method()





#constructor example
class students:
    def __init__(self,name):
        self.name=name
        print("parent class constructor")
class child(students):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    print("child class constructor")

c=child("Riya",20)
print(c.name)
print(c.age)
