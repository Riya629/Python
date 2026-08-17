# # #Without using shortcut
# # class Employee:
# #     def __init__(self):
# #         self._age=0
# #     def set_age(self,age):
# #         self._age=age
# #     def get_age(self):
# #         return self._age
# # e=Employee()
# # e.set_age(20)
# # print(" Age:",e.get_age())


# class Employee:
#     def __init__(self):
#         self.__name=""
#     def set_name(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name
# e=Employee()
# e.set_name("Riya")
# print("Name:",e.get_name())



# #Using shortcut for getter and setter

# class person:
#     def __init__(self):
#         self.__age=0
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,age):
#         self.__age=age
# p=person()
# p.age=20
# print("Age:",p.age)







# class employee:
#     def__init__(self):
#         self.__age=0
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,age):
#         self.__age=age


